#!/usr/bin/python
#
import requests
import mysql.connector
import datetime
import serial
from time import sleep

def getserial():
  res = ("0","0","0");
  try:
    ser = serial.Serial(0, 9600)
    #ser.open()
    if (ser.isOpen()):
      ser.write("a")
      sleep(0.1)
      ln1 = ser.readline()
      ln2 = ser.readline()
      ln3 = ser.readline()
      res = (ln1,ln2,ln3);
      
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

  r = requests.post("http://emoncms.org/input/post?json={power:"+str(val[0])+"}&apikey=7ac88045c3f843febe32d0d75d7b8a72")
  r = requests.post("http://emoncms.org/input/post?json={power:"+str(val[1])+"}&apikey=7ac88045c3f843febe32d0d75d7b8a72")
  r = requests.post("http://emoncms.org/input/post?json={power:"+str(val[2])+"}&apikey=7ac88045c3f843febe32d0d75d7b8a72")

  try:
    c.execute('USE bolejka;') 
    c.execute('INSERT INTO mesurements (mesuredatetime, sensorid, value) VALUES ("'+curdate+'",1,'+str(val[0])+');')
    c.execute('INSERT INTO mesurements (mesuredatetime, sensorid, value) VALUES ("'+curdate+'",2,'+str(val[1])+');')
    c.execute('INSERT INTO mesurements (mesuredatetime, sensorid, value) VALUES ("'+curdate+'",3,'+str(val[2])+');')
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


