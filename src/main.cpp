#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); 
  pinMode(PIN0, INPUT);

  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int inputValue;
  inputValue = digitalRead(PIN0);
  digitalWrite(LED_BUILTIN, inputValue);
  Serial.write("Hello! \n");
  delay(10);
}