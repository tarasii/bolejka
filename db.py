#!/usr/bin/python
#

import mysql.connector

def createtables():
  try:
    conn = mysql.connector.connect(host="localhost", 
                     user="root", 
                      passwd="aceofbase")  
  except:
    print ("Error connection")
    return

  c = conn.cursor()

  try:
    c.execute('CREATE DATABASE IF NOT EXISTS bolejka;')
    c.execute('SHOW DATABASES;')
    print c.fetchall()
    c.execute('USE bolejka;')
    c.execute('DROP TABLE IF EXISTS sensors;')
    c.execute('CREATE TABLE sensors(id INT(11) AUTO_INCREMENT, name TEXT, PRIMARY KEY(id));')

    c.execute('DROP TABLE IF EXISTS mesurements;')
    c.execute('CREATE TABLE mesurements(id INT(11) AUTO_INCREMENT, mesuredatetime DATETIME, sensorid INT, value FLOAT(12,2), javadatetime TEXT, PRIMARY KEY(id));')
    c.execute('SHOW TABLES;')
    print c.fetchall()
    c.execute('SHOW COLUMNS FROM sensors;')
    print c.fetchall()
    c.execute('SHOW COLUMNS FROM mesurements;')
    print c.fetchall()
    c.execute('INSERT INTO sensors (name) VALUES ("Main current sensor");')
    c.execute('SELECT * FROM sensors;')
    print c.fetchall()
  except:
    print ("Error command")
    conn.close()
    return
  
  conn.commit()

  conn.close()
  return


if __name__ == "__main__":
  createtables()