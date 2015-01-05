#!/usr/bin/python
#

import mysql.connector
import datetime
import serial


def getserial():
  res = "0";
  ser = serial.Serial(0, 9600)
  try:
    ser.open()
    if (ser.isOpen()):
      line = ser.readline()
      ser.close()

  except:
    print ("Error comm")

  return res


def writetable(val):
  try:
    conn = mysql.connector.connect(host="localhost", 
                     user="root", 
                      passwd="aceofbase")  
  except:
    print ("Error connection")
    return

  c = conn.cursor()

  curdate = str(datetime.datetime.now())

  try:
    c.execute('USE bolejka;') 
    c.execute('INSERT INTO mesurements (mesuredatetime, sensorid, value) VALUES ("'+curdate+'",1,'+str(val)+');')
    c.execute('SELECT * FROM mesurements;')
    print c.fetchall()
  
  except:
    print ("Error command")
    conn.close()
    return
  

  conn.commit()
  conn.close()
  return


if __name__ == "__main__":
  val = getserial() 
  writetable(val)