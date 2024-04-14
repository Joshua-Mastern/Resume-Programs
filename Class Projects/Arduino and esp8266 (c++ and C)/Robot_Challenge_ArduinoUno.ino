#include <Servo.h> 
Servo servoL;   
Servo servoR;
int white=800;     
int black=730;     

int button1 = 11;
int b1Pressed = 0;
int button2 = 10;
int b2Pressed = 0;

int ledRed = 3;
int ledGreen = 5;
int ledYellow = 7;
int ledGO = 8;


void setup() {  
    servoL.attach(13);
    servoR.attach(2);
    
    pinMode (button1, INPUT);
    pinMode (button2, INPUT);
    
    pinMode (ledRed, OUTPUT);
    pinMode (ledGreen, OUTPUT);
    pinMode (ledYellow, OUTPUT);

    pinMode (ledGO, OUTPUT);
    Serial.begin(9600);
} 

void loop() { 
   int b2 = digitalRead(button2);
  
  int val = analogRead(5);
       Serial.print("white = ");    Serial.print(white);
       Serial.print("   black = "); Serial.print(black);
       Serial.print("   val = ");   Serial.println(val);
   
   //cycle button1
   cycleButton1();
   //cycle button 2
   cycleButton2(b2);
   
   //main part
   if(b2Pressed == 0){
    //if b2Presse is equal to 0 light up red led and do nanosystems and mechanical engineering challenge
    digitalWrite(ledRed, HIGH); digitalWrite(ledGreen, LOW); digitalWrite(ledYellow, LOW);
      if(b1Pressed == 1){
          b1Pressed = nanoSystems(); //will return value 0 when completed stopping robot
      }
   }  else if (b2Pressed == 1){
            // when it equals one then light up green and do electrical engineering challenge
            digitalWrite(ledGreen,HIGH);digitalWrite(ledRed,LOW);digitalWrite(ledYellow,LOW);
            if(b1Pressed == 1){
                b1Pressed = electricalEngr();//will return value 0 when completed stopping robot
            }
       }  else if (b2Pressed == 2){
                //when it equals 2 light up yellow led and do cyberEngineering challeng
                digitalWrite(ledYellow,HIGH); digitalWrite(ledRed,LOW); digitalWrite(ledGreen,LOW);
                if(b1Pressed == 1){
                  
                  b1Pressed = cyberEngr();//will return value 0 when completed stopping robot
                  
                }
            }
}

void guide(int left, int right){
  //function to control robot movement with, the integers passed to it become the values for left and right servos
  servoL.writeMicroseconds(left); //1600 for cw
  servoR.writeMicroseconds(right); //1400 for cw
  
}

void followRight(){
  //follow on the right side of the line
  bool unDone = true;
  int val = analogRead(5);
  while (unDone){
        val = analogRead(5);
       Serial.print("white = ");    Serial.print(white);
       Serial.print("   black = "); Serial.print(black);
       Serial.print("   val = ");   Serial.println(val);
       
      if      (val>white)   {guide(1440,1430);   }  // over white slow left
       else if (val<black)   {guide(1570,1560);    }// over black slow right
       else {guide(1580,1420);} //slow forward
  }
}

void cycleButton1(){ 
  //allow adjusting for the value of button1, when it exceeds 1 return it to zero
  if(digitalRead(button1)){
    b1Pressed = b1Pressed + 1;
    delay(500);
  }
  if(b1Pressed > 1){
    b1Pressed = 0;
  }
  if(b1Pressed == 1){
    digitalWrite(ledGO, HIGH);
  } else {digitalWrite(ledGO, LOW);}
  
}

void cycleButton2(int b2){
  //allow adjusting of value for button2 and if it exceeds 2 reset to 0
  if( 1 == b2){
    b2Pressed = b2Pressed+1;
    delay(500);
  }
  if(b2Pressed > 2){
    b2Pressed = 0;
  }

}

int nanoSystems(){
  //do nanoSystems and mechanical engineering challenge
  
  //move straight forward
  guide(1670,1000);
  delay(1200);

  //halt
  guide(1500,1500);

  //move backward
  guide(1200, 1800);
  delay (800);

  //halt 
  guide(1500,1500);
  delay(350);

  //swoop retrieve
  guide(1950, 1450);
  delay(1400);

  //return straight
  guide(1800,1200);
  delay (900);

  //halt
  guide(1500,1500);
  
  
   //will set button1 to off
   return 0;
}

int electricalEngr(){
  //do electrical engineering challenge
  //move straight forward
  guide(1800,1200);
  delay(1100);

  //halt
  guide(1500,1500);

  //move backward
  guide(1200, 1800);
  delay (1300);

  //halt
  guide (1500, 1500);
   //will set button1 to off

  return 0; //will set button1 to off
}
int cyberEngr(){
  //do cyber engineering challenge
  //go forward to reach black line
   guide(1600, 1380);
   delay(2600); 
  //start following line
   followRight();

  return 0; //will set button1 to off
}
