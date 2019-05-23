#include <LiquidCrystal.h>

String youtube_name = "";                                                       //your youtube name
String youtube_token = "AIzaSyA0GTEKH_HKDVbYSepq5D2Bm_WDSPmIwh8";              //your youtube token
String instagram_token ="";                                                   //your instagram token
unsigned long DELAY= 10;                                                     //delay between to screen (seconds)
//set lcd screen pins
const int rs = 8, en = 9, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
//create variables
unsigned long follower = 0,follower2=0,subscriber=0,subscriber2=0,x=millis();
//create bytes for logos
byte instagram1[8] = {0b00000,0b01111,0b10000,0b10000,0b10000,0b10000,0b10000,0b11111};
byte instagram2[8] = {0b00000,0b11111,0b00000,0b00000,0b00000,0b00000,0b01110,0b10001};
byte instagram3[8] = {0b00000,0b11110,0b00001,0b11001,0b11001,0b00001,0b00001,0b11111};
byte instagram4[8] = {0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b01111};
byte instagram5[8] = {0b10001,0b10001,0b01110,0b00000,0b00000,0b00000,0b00000,0b11111};
byte instagram6[8] = {0b00001,0b00001,0b00001,0b00001,0b00001,0b00001,0b00001,0b11110};
byte youtube1[8] =   {0b11111,0b11100,0b11000,0b10000,0b10000,0b10000,0b10000,0b10000};
byte youtube2[8] =   {0b11111,0b00000,0b10000,0b11000,0b11100,0b11110,0b11111,0b11111};
byte youtube3[8] =   {0b11111,0b00111,0b00011,0b00001,0b00001,0b00001,0b00001,0b10001};
byte youtube4[8] =   {0b10000,0b10000,0b10000,0b10000,0b10000,0b11000,0b11100,0b11111};
byte youtube5[8] =   {0b11111,0b11111,0b11110,0b11100,0b11000,0b10000,0b00000,0b11111};
byte youtube6[8] =   {0b10001,0b00001,0b00001,0b00001,0b00001,0b00011,0b00111,0b11111};
void setup() {
  lcd.begin(16, 2);                      //start lcd
  Serial.begin(9600);                   //start serial communication
  delay(2000);                        
  Serial.println(youtube_name);       //say variables to program
  delay(1000);
  Serial.println(youtube_token);    //say variables to program
  delay(1000);
  Serial.println(instagram_token);//say variables to program
}

void loop() { 
  
  if(x<(DELAY*1000)){
  drawinstagram();
  lcd.setCursor(5,1);
  lcd.print(follower);
  while(x<(DELAY*1000) && follower2 == follower){
      while(Serial.available()>0){
        follower2=Serial.parseInt();
        subscriber2=Serial.parseInt();
        }
      x = millis();
      x = x%(DELAY*2000);
      }
      subscriber=subscriber2;
      follower=follower2;
  }

  
  else{
  drawyoutube();
  lcd.setCursor(5,1);
  lcd.print(subscriber);
  while(x>=(DELAY*1000) && subscriber2 == subscriber){
     while(Serial.available()>0){
        follower2=Serial.parseInt();
        subscriber2=Serial.parseInt();
        }
      x = millis();
      x = x%(DELAY*2000);
    }
    subscriber=subscriber2;
    follower=follower2;
  }
}

//draw instagram logo
void drawinstagram(){
  lcd.createChar(0,instagram1);
  lcd.createChar(1,instagram2);
  lcd.createChar(2,instagram3);
  lcd.createChar(3,instagram4);
  lcd.createChar(4,instagram5);
  lcd.createChar(5,instagram6);
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.write(byte(0)); 
  lcd.write(byte(1));
  lcd.write(byte(2));
  lcd.setCursor(1,1);
  lcd.write(byte(3)); 
  lcd.write(byte(4));
  lcd.write(byte(5));
  lcd.setCursor(5,0);
  lcd.print("Followers");
  }

//draw youtubelogo
void drawyoutube(){
  lcd.createChar(6,youtube1);
  lcd.createChar(7,youtube2);
  lcd.createChar(8,youtube3);
  lcd.createChar(9,youtube4);
  lcd.createChar(10,youtube5);
  lcd.createChar(11,youtube6);
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.write(byte(6)); 
  lcd.write(byte(7));
  lcd.write(byte(8));
  lcd.setCursor(1,1);
  lcd.write(byte(9)); 
  lcd.write(byte(10));
  lcd.write(byte(11));
  lcd.setCursor(5,0);
  lcd.print("Subscribers");
  }
