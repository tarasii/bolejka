#!/usr/bin/python
#
import requests
import mysql.connector
import datetime
import serial
from time import sleep

def getserial():
  res = "0";
  ser = serial.Serial(0, 9600)
  try:
    ser.open()
    if (ser.isOpen()):
      ser.write("a")
      sleep(0.1)
      line = ser.readline()
      ser.close()

  except:
    print ("Error comm")

  return res


def writetable(val):
  try:
    conn = mysql.connector.connect(host="localhost", 
                     user="root", 
                      passwd="")  
  except:
    print ("Error connection")
    return

  c = conn.cursor()

  curdate = str(datetime.datetime.now())

  r = requests.post("http://emoncms.org/input/post?json={power:"+str(val)+"}&apikey=7ac88045c3f843febe32d0d75d7b8a72")

  try:
    c.execute('USE bolejka;') 
    c.execute('INSERT INTO mesurements (mesuredatetime, sensorid, value) VALUES ("'+curdate+'",1,'+str(val)+');')
    #c.execute('SELECT * FROM mesurements;')
    #print c.fetchall()
  
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
