void setup() {
  pinMode(4, INPUT);
  Serial.begin(9600);
  tone(8,38000); 
}
 
void loop() {
  int detect=digitalRead(4);
  Serial.println(detect);
}
