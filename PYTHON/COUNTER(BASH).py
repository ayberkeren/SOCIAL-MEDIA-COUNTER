import urllib.request                           #for make web requests
import json                                     #for encode and decode json files
import serial                                   #for serial communication
import sys                                      #for recognize operating system
import time                                     #for delays
from serial import Serial                      
import os,ssl

print("Social Media Counter")
print("Made by Ayberk Eren")

#this function try each serial port and find availables
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(20)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(str(port))
        except (OSError, serial.SerialException):
            pass
    return result


#print port list 
print("PORTS :" + str(serial_ports()))
arduino = input("ENTER PORT:")
#start communication with arduino
arduino = serial.Serial(arduino,9600)

#read youtube user name from serial and decode
name = (arduino.readline())
name=name.decode('utf-8')
name=name[0:-2]
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


while True:
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
    arduino.write(str.encode(output))
    #wait 10 seconds before starts again
    time.sleep(10) 

