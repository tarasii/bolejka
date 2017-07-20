#!/usr/bin/python
#

import mysql.connector
import datetime
import serial
from time import sleep

def getserial():
  res = "0";
  ser = serial.Serial(0, 9600)
  try:
    #ser.open()
    if (ser.isOpen()):
      ser.write("a")
      sleep(0.1)
      line = ser.readline()
      ser.close()

  except Exception as e:
    print "Error comm", e

  return res



if __name__ == "__main__":

  while (1==1):
     val = getserial() 
     print val
     sleep(1)
     
