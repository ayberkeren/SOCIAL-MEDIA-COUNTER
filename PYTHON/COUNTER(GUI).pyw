from tkinter import*                            #for gui
import urllib.request                           #for make web requests
import json                                     #for encode and decode json files
import serial                                   #for serial communication
import sys                                      #for recognize operating system
import time                                     #for delays
from serial import Serial                      


def run(port):
    #create variables
    global arduino           
    global name
    global key
    global token
    #stop variables for exit refreshing loop
    global stop
    stop=False
    #start communication with arduino
    arduino= serial.Serial(port,9600)
    #read youtube user name from serial
    name = (arduino.readline())
    #decode name
    name=name.decode('utf-8')
    name=name[0:-2]
    #print username to bash
    print("YOUTUBE USERNAME:"+name)

    #read youtube token from serial and decode
    key = (arduino.readline())
    key=key.decode('utf-8')
    key=key[0:-2]
    print("YOUTUBE TOKEN:"+key)

    #read instagram token from serial and decode
    token = (arduino.readline())
    token=token.decode('utf-8')
    token=token[0:-2]
    print("INSTAGRAM TOKEN:"+token)
    
    window.after(1000,refresh)


#this function pull follower and subscribers numbers from web and print on gui and bash
def refresh():
    global token,key,name,arduino,stop
    #make request for youtube subscriber number
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
    #decode data and pick number of subscribers
    subs = json.loads(data.decode('utf-8'))["items"][0]["statistics"]["subscriberCount"]
    #make request for instagram follower
    data2 = urllib.request.urlopen("https://api.instagram.com/v1/users/self/?access_token="+token).read()
    #decode data and pick number of follower
    follower = json.loads(data2.decode('utf-8'))["data"]["counts"]["followed_by"]
    #prepare data for arduino
    output =str(follower)+" "+str(subs)
    #print data on the bash
    print("--------------------------------------------------------------------")
    print("INSTAGRAM FOLLOWER:",str(follower),"      ","YOUTUBE SUBSCRIBER:",str(subs))
    #print data on the gui
    yt_subscriber["text"]=str(follower)
    ig_follower["text"]=str(subs)
    #send data to arduino
    arduino.write(str.encode(output))
    #update gui screen
    window.update()
    #refresh the data every 5 seconds
    if stop == False:
        window.after(5000,refresh)
    #if user press to list button exit from loop 
    else:
        arduino.close()


#this function pick selected port
def select():
    print(portlist.get(ACTIVE))
    selectbuton["state"]="disabled"
    run(portlist.get(ACTIVE))

#this function try each serial port and find availables
def list():
    global stop
    stop=True
    portlist.delete(0,END)
    selectbuton["state"]="normal"
    ports = ['COM%s' % (i + 1) for i in range(20)]
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            portlist.insert(END,port)
        except (OSError, serial.SerialException):
            pass



#creating gui
window =Tk()
#give title to window
window.title("Social Media Counter")
#set window size to 300 px,250 px and location start from 0 , 0
window.geometry("300x250+0+0")
#set window resizable on x and y axis
window.resizable(0,0)
#give transparency
window.wm_attributes("-alpha",0.99)
#set window background white
window.configure(background='white')

#portlist
portlist=Listbox(
    selectmode="BROWSE",
    justify="center",
    font=("Open Sans","12","bold")
    )
portlist.pack(
    side="left",
     anchor="n",
    )
portlist.place(
    height=100,
    width=195,
    x=5,
    y=5
    )

selectbuton=Button(
    text="SELECT",
    command=select,
    padx=20,
    pady=9,
    state="normal",
    bg="black",
    fg="white",
    font=("Open Sans","12","bold"),
    disabledforeground="gray"
    )

selectbuton.pack()

selectbuton.place(
    width=90,
    height=45,
    x=205,
    y=60
    )

listbuton=Button(
    text="LIST",
    command=list,
    padx=20,
    pady=9,
    bg="black",
    fg="white",
    font=("Open Sans","12","bold")
    )

listbuton.pack()

listbuton.place(
    width=90,
    height=45,
    x=205,
    y=5
    )


ig_text=Label(
    text="IG:",
    font=("Open Sans","24","bold"),
    justify="center",
    fg="black",
    bg="white"
    )

ig_text.pack()
ig_text.place(
    x=5,
    y=110,
    )

yt_text=Label(
    text="YT:",
    font=("Open Sans","24","bold"),
    justify="center",
    fg="black",
    bg="white"
    )

yt_text.pack()
yt_text.place(
    x=5,
    y=180,
    )

ig_follower=Label(
    text="0",
    font=("Open Sans","24","bold"),
    justify="left",
    fg="black",
    bg="white"
    )

ig_follower.pack()
ig_follower.place(
    x=60,
    y=110,
    )

yt_subscriber=Label(
    text="0",
    font=("Open Sans","24","bold"),
    justify="left",
    fg="black",
    bg="white"
    )

yt_subscriber.pack()
yt_subscriber.place(
    x=60,
    y=180,
    )


#this for window stay open
mainloop()
