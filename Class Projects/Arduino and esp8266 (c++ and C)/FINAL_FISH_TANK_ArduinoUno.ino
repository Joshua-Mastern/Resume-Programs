#include <SoftwareSerial.h>                    // use the software serial library
   SoftwareSerial mySerial(3,2);               // receive data at pin 3; transmit data at pin 2
   
int val = 0;
int UCLHeater = 511;
int setPointHeater = 505;
int LCLHeater = 498;

int deadTime = 11000;
float gain = 0.7;
float QNaCl = 6.305; //flowrate for NaCl valve in grams
float QDI = 4.645; //flowrate for DI valve in grams

long DItimer = 0;
long NaClTimer = 0;
long currentTime = 0;
long holdDI = 0;
long holdNaCl = 0;

float sal = 0;
int UCL = 633;
int setpoint = 625;
int LCL = 617;

int salLog[10];
int iLog = 0;


void setup() {
   pinMode(8, OUTPUT); pinMode(4, OUTPUT); pinMode(10, OUTPUT); pinMode(9, OUTPUT);
   mySerial.begin(9600); delay(500);  
   Serial.begin(9600);
   startLCD();
}

void loop() {
  val = analogRead(5);                         // set the variable 'val' to the value read by analog pin 5       
  digitalWrite(4, HIGH);
  delay(100);
  sal = analogRead(4);
  digitalWrite(4, LOW);
  delay(1000);
  
  float temper = analogToTemp(val);
  float percentSal=analogToSalinity(sal);
  mySerial.write(254); mySerial.write(214);
  mySerial.print(percentSal, 3);
  if(val > UCLHeater)                            
  {
    heatOff();                                
    mySerial.write(254); mySerial.write(222);
    mySerial.print(temper, 1);         
    mySerial.write(254); mySerial.write(229);  
    mySerial.write("OFF");                     
  }
  else if(val < LCLHeater)                      
  {
    heatOn();                                 
    mySerial.write(254); mySerial.write(222);  
    mySerial.print(temper, 1);         
    mySerial.write(254); mySerial.write(229);
    mySerial.write("ON ");                     
  }
  else                                        
  {
    mySerial.write(254); mySerial.write(222);  
    mySerial.print(temper, 1);         
    
  }
  
  currentTime = millis();
  DItimer = currentTime - holdDI;
  NaClTimer = currentTime -holdNaCl;

  //a log shall be kept no greater than 10 elements
  if(iLog>9)
  {
    iLog = 0;
  }

  salLog[iLog] = {sal};
  Serial.println(salLog[iLog]);
  //check to see what needs to be opened
  //if we need to we can say deadTime+ time the valve was open for
  if(sal > UCL && salLog[iLog-1] >UCL && DItimer > deadTime)
  {
    //calculate target
    float tempTarget = computeTarget(percentSal);

    //calculate time open
    float tempTime = computeTimeDI(percentSal, tempTarget);
    Serial.println(tempTime);
    Serial.println(tempTarget);
    DIValve(tempTime);
  }else if(sal < LCL && salLog[iLog-1] < LCL && NaClTimer > deadTime)
  {
    //calculate target
    float tempTarget = computeTarget(percentSal);

    //calculate time open
    float tempTime = computeTimeNaCl(percentSal, tempTarget);
    Serial.println(tempTime);
    Serial.println(tempTarget,3);
    NaClValve(tempTime);
  }
  //increment ilog
  iLog= iLog+1;
}

void heatOn() {                              
    digitalWrite(8, HIGH);                     // turns on heater
  }

void heatOff() {
    digitalWrite(8, LOW);                      // turns off heater
  }

void startLCD() {         
   mySerial.write(254);  mySerial.write(1);    
   mySerial.write(254);  mySerial.write(132); 
   mySerial.write("LCL    SP   UCL");            
   mySerial.write(254);  mySerial.write(192);   
   mySerial.write("S: 0.093 0.100 0.108");
   mySerial.write(254);  mySerial.write(148);
   mySerial.write("T:  24.2  25.0  25.7");
   mySerial.write("S=");
   mySerial.write(254); mySerial.write(220);
   mySerial.write("T=");
   mySerial.write(254); mySerial.write(227);
   mySerial.write("H=");
  }

float computeTarget(float currentSalinity){
  float setpointPercent = analogToSalinity(setpoint);
  float error = currentSalinity - setpointPercent;
  float targetSalinity = currentSalinity-error*gain;
  return targetSalinity;
}

float computeTimeNaCl(float currentSalinity, float targetSalinity){
  //get them in fractal form
  currentSalinity = currentSalinity/100;
  targetSalinity = targetSalinity/100;
  
  //calculate how many g of water needs to be added
  float temp = 72.2*currentSalinity-72.2*targetSalinity;
  float x = temp/((0.85*currentSalinity)-0.0085);
  
  //calculate how long it needs to be open to get that many g
  float timeOpen = x/QNaCl;
  timeOpen = timeOpen*1000; // convert to millis
  return timeOpen;
}

float computeTimeDI(float currentSalinity, float targetSalinity){
  //get them in fractal form
  currentSalinity = currentSalinity/100;
  targetSalinity = targetSalinity/100;
  
  //calculate how many g of water needs to be added
  float temp = 72.2*currentSalinity-72.2*targetSalinity;
  float x = temp/(0.85*currentSalinity);

  //calculate how long it needs to be open to get that many g
  float timeOpen = x/QDI;
  timeOpen = timeOpen*1000; // convert to millis
  return timeOpen;
}

void DIValve(float timeOpen) 
{
    Serial.println("Entering DIValve function   ");
    digitalWrite(9, HIGH); delay(timeOpen);
    digitalWrite(9, LOW);
    Serial.print("DI Valve Opened for "); Serial.print(timeOpen/1000);
    Serial.print(" seconds, starting deadtime= ");Serial.println(deadTime/1000);
    holdDI = millis();
    holdNaCl= millis();
    
    Serial.println("Exiting DIValve function");
}
void NaClValve(float timeOpen)
{
  Serial.println("Entering NaClValve function    ");
  
  digitalWrite(10, HIGH); 
  delay(timeOpen);
  digitalWrite(10, LOW);

  Serial.print("NaCl Valve Opened for "); Serial.print(timeOpen/1000);
  Serial.print(" seconds, starting deadtime= ");Serial.println(deadTime/1000);

  holdDI = millis();
  holdNaCl= millis();
  Serial.println("Exiting NaClValve function");
}

  
float analogToSalinity(int analog)
{
  float temp = 8*pow(10, -18);
  float salinity = temp*pow(analog,5.7584);
  return salinity;
  
}

float analogToTemp(int analog)
{
  float temperature = (0.1092*analog-30.159);
  return temperature;
}

  
  

  
