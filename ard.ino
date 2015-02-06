// EmonLibrary examples openenergymonitor.org, Licence GNU GPL V3

#include "EmonLib.h"                   // Include Emon Library
EnergyMonitor emon1;                   // Create an instance
EnergyMonitor emon2;                   // Create an instance
EnergyMonitor emon3;                   // Create an instance
int incomingByte;
int val;

void setup()
{  
  Serial.begin(9600);
  
  emon1.current(1, 85);             // Current: input pin, calibration.
  emon2.current(2, 85);             // Current: input pin, calibration.
  emon3.current(3, 85);             // Current: input pin, calibration.
}

void loop()
{
  double Irms1 = emon1.calcIrms(1800);  // Calculate Irms only
  double Irms2 = emon2.calcIrms(1800);  // Calculate Irms only
  double Irms3 = emon3.calcIrms(1800);  // Calculate Irms only

  //Serial.print(Irms*230.0);	       // Apparent power
  //Serial.print(" ");
  
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    Serial.println(Irms1);		       // Irms
    Serial.println(Irms2);		       // Irms
    Serial.println(Irms3);		       // Irms
    
  }
}
