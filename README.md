bolejka
=======

Script 'db.py' creates database 'boejka'

mysql> show tables;
+-------------------+
| Tables_in_bolejka |
+-------------------+
| mesurements       |
| sensors           |
+-------------------+
2 rows in set (0.00 sec)

mysql> show columns in sensors;
+-------+---------+------+-----+---------+----------------+
| Field | Type    | Null | Key | Default | Extra          |
+-------+---------+------+-----+---------+----------------+
| id    | int(11) | NO   | PRI | NULL    | auto_increment |
| name  | text    | YES  |     | NULL    |                |
+-------+---------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> show columns in mesurements;
+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| id             | int(11)     | NO   | PRI | NULL    | auto_increment |
| mesuredatetime | datetime    | YES  |     | NULL    |                |
| sensorid       | int(11)     | YES  |     | NULL    |                |
| value          | float(12,2) | YES  |     | NULL    |                |
| javadatetime   | text        | YES  |     | NULL    |                |
+----------------+-------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

sript 'ser.py' sends a char to comm and receive ansver from device 

'ard.ino' is a source code for device
