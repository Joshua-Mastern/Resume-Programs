float freqC4 = 261.63;
int periodC4;
int halfC4;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  periodC4 = 1/(freqC4*1000000);
  halfC4 = periodC4/2;

}

void loop() {
  // put your main code here, to run repeatedly:
 // digitalWrite(13, HIGH); delayMicroseconds(halfC4);
 // digitalWrite(13,LOW); delayMicroseconds(halfC4); 
 tone(13, 1500);
 delay(1000);
 noTone(13);
 delay (1000);

}
