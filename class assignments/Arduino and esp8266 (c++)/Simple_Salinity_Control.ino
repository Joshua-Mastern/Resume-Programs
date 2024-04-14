long DItimer = 0;
long NaClTimer = 0;
long currentTime = 0;
long holdDI = 0;
long holdNaCl = 0;

float UCL = 555.2605;
float setpoint = 550.7629;
float LCL = 546.2653;

int val = 0;



void setup() 
{
  Serial.begin(9600);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(4, OUTPUT);

}

void loop() 
{
  digitalWrite(4, HIGH);
  delay(100);
  val = analogRead(4);
  digitalWrite(4, LOW);
  Serial.print("Salinity Analog Value: ");
  Serial.print(val);
  Serial.print("    Salinity percent value: ");
  Serial.println(analogToSalinity(val));
  
  currentTime = millis();
  DItimer = currentTime - holdDI;
  NaClTimer = currentTime - holdNaCl;
  Serial.print("Time since program has started:   ");
  Serial.print(currentTime);
  Serial.print("    DITimer = "); Serial.print(DItimer);
  Serial.print("    NaClTimer = "); Serial.println(NaClTimer);
  if(val > UCL && DItimer > 10000)
  {
    DIValve();
  }else if(val < LCL && NaClTimer > 10000)
  {
    NaClValve();
  }
  
  delay(1500);
}

void DIValve() 
{
  
  Serial.print("Entering DIValve function   ");
    
    digitalWrite(9, HIGH); delay(1000);
    digitalWrite(9, LOW);
    holdDI = millis();
    Serial.print("DI Valve Opened for 0.5s, starting 10s timer");
  
  Serial.println("Exiting DIValve function");
}

void NaClValve()
{
  Serial.print("Entering NaClValve function    ");
  
  digitalWrite(10, HIGH); 
  delay(500);
  digitalWrite(10, LOW);
  holdNaCl = millis();
  Serial.print("NaCl Valve Opened for 0.5s, starting 10s timer ");
  
  Serial.println("Exiting NaClValve function");
}

float analogToSalinity(int analog)
{
  float temp = 2*pow(10, -20);
  float salinity = temp*pow(analog,6.7997);
  return salinity;
  
}
