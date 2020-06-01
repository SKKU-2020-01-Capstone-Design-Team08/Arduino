#include <SoftwareSerial.h>
 
SoftwareSerial gpsSerial(3,2);
 
void setup() {
  Serial.begin(9600);
  Serial.println("Start GPS... ");
  gpsSerial.begin(9600);
}
 
void loop() {
  if(gpsSerial.available())
  {
    Serial.write(gpsSerial.read());
  }
}
