
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(22, INPUT);
  pinMode(24, INPUT);
  pinMode(26, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("22 is");
  Serial.println(digitalRead(22));
  
}
