#include <Arduino.h>

int inputValue = 0;
// messages with key code
char key_code [136] = {0,0,  1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 0,0,0,0,
                              0,0,1,0, 0,0,0,0, 0,0,0,0, 1,0,0,1, 0,1,1,1,
                              0,1,0,1, 1,1,0,0, 1,0,1,1, 1,1,1,1, 1,1,1,1,
                              1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1,
                              1,1,1,1, 1,1,1,0, 1,0,0,0, 1,1,1,0, 1,0,1,0,
                              0,1,0,1, 0,0,0,0, 0,0,1,1, 1,1,1,1, 1,1,1,1,
                              1,1,1,1, 1,1,1,0, 1,1,1,1, 1,1};

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); 
  pinMode(PIN0, INPUT);
  Serial.begin(9600);
  Serial.println("Hello!");
}

void loop() {
  // put your main code here, to run repeatedly:
  
  inputValue = digitalRead(PIN0);
  digitalWrite(LED_BUILTIN, inputValue);
  Serial.println("1");
  delay(10);
}