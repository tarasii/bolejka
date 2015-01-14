// EmonLibrary examples openenergymonitor.org, Licence GNU GPL V3

#include "EmonLib.h"                   // Include Emon Library
EnergyMonitor emon1;                   // Create an instance
int incomingByte;
int val;

void setup()
{  
  Serial.begin(9600);
  
  //emon1.current(1, 111.1);             // Current: input pin, calibration.
}

void loop()
{
  //double Irms = emon1.calcIrms(1480);  // Calculate Irms only
  
  //Serial.print(Irms*230.0);	       // Apparent power
  //Serial.print(" ");
  
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    //Serial.println(Irms);		       // Irms
    
    val = analogRead(0);     // считываем значение
    Serial.print("А0=");
    Serial.println(val);             // выводим полученное значение
    
    val = analogRead(1);     // считываем значение
    Serial.print("А1=");
    Serial.println(val);             // выводим полученное значение
    
    val = analogRead(2);     // считываем значение
    Serial.print("А2=");
    Serial.println(val);             // выводим полученное значение
    
  }
}
