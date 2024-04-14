void setup() {
  // put your setup code here, to run once:
  pinMode(8,OUTPUT); // right servo connected
  pinMode(12,OUTPUT);//left serco connected
}

void loop() {
  // put your main code here, to run repeatedly:
 for (int i = 0; i < 200; i++){
     //right servo
     digitalWrite(8, HIGH);
     delayMicroseconds(1000);
     digitalWrite(8, LOW);
     delay(20);
     //left servo
     digitalWrite(12, HIGH);
     delayMicroseconds(2000);
     digitalWrite(12, LOW);
     delay(20);
 }
delay(1000);
//wide left turn
for (int i = 0; i <150; i++){
    //right servo
    digitalWrite(8, HIGH);
    delayMicroseconds(1000);
    digitalWrite(8, LOW);
    delay(20);
    //left servo
    digitalWrite(12, HIGH);
    delayMicroseconds(1600);
    digitalWrite(12, LOW);
    delay(20);
    
}
delay(1000);

}
