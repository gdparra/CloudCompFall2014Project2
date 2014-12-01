import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3

conn = sqlite3.connect('solarenergyplant.db')
c=conn.cursor()

#for row in c.execute('SELECT * FROM solardata'):
#	print row
c.execute("DROP TABLE IF EXISTS PLANTMAIN")
c.execute("DROP TABLE IF EXISTS PLANTCITY")
c.execute("DROP TABLE IF EXISTS PLANTPANEL")
c.execute("DROP TABLE IF EXISTS PANELSENSOR")
c.execute("DROP TABLE IF EXISTS CITYADDRESS")
c.execute("DROP TABLE IF EXISTS P1DATES")
c.execute("DROP TABLE IF EXISTS P2DATES")
c.execute("DROP TABLE IF EXISTS P3DATES")
c.execute("DROP TABLE IF EXISTS P4DATES")
c.execute("DROP TABLE IF EXISTS P1M1TEMP")
c.execute("DROP TABLE IF EXISTS P1M2TEMP")
c.execute("DROP TABLE IF EXISTS P1M3TEMP")
c.execute("DROP TABLE IF EXISTS P2M1TEMP")
c.execute("DROP TABLE IF EXISTS P2M2TEMP")
c.execute("DROP TABLE IF EXISTS P2M3TEMP")
c.execute("DROP TABLE IF EXISTS P3M1TEMP")
c.execute("DROP TABLE IF EXISTS P3M2TEMP")
c.execute("DROP TABLE IF EXISTS P3M3TEMP")
c.execute("DROP TABLE IF EXISTS P4M1TEMP")
c.execute("DROP TABLE IF EXISTS P4M2TEMP")
c.execute("DROP TABLE IF EXISTS P4M3TEMP")
c.execute("DROP TABLE IF EXISTS P1M1Irradiance")
c.execute("DROP TABLE IF EXISTS P1M2Irradiance")
c.execute("DROP TABLE IF EXISTS P1M3Irradiance")
c.execute("DROP TABLE IF EXISTS P2M1Irradiance")
c.execute("DROP TABLE IF EXISTS P2M2Irradiance")
c.execute("DROP TABLE IF EXISTS P2M3Irradiance")
c.execute("DROP TABLE IF EXISTS P3M1Irradiance")
c.execute("DROP TABLE IF EXISTS P3M2Irradiance")
c.execute("DROP TABLE IF EXISTS P3M3Irradiance")
c.execute("DROP TABLE IF EXISTS P4M1Irradiance")
c.execute("DROP TABLE IF EXISTS P4M2Irradiance")
c.execute("DROP TABLE IF EXISTS P4M3Irradiance")
c.execute("DROP TABLE IF EXISTS P1M1Watts")
c.execute("DROP TABLE IF EXISTS P1M2Watts")
c.execute("DROP TABLE IF EXISTS P1M3Watts")
c.execute("DROP TABLE IF EXISTS P2M1Watts")
c.execute("DROP TABLE IF EXISTS P2M2Watts")
c.execute("DROP TABLE IF EXISTS P2M3Watts")
c.execute("DROP TABLE IF EXISTS P3M1Watts")
c.execute("DROP TABLE IF EXISTS P3M2Watts")
c.execute("DROP TABLE IF EXISTS P3M3Watts")
c.execute("DROP TABLE IF EXISTS P4M1Watts")
c.execute("DROP TABLE IF EXISTS P4M2Watts")
c.execute("DROP TABLE IF EXISTS P4M3Watts")
c.execute("DROP TABLE IF EXISTS P1T1IrradTime")
c.execute("DROP TABLE IF EXISTS P2T1IrradTime")
c.execute("DROP TABLE IF EXISTS P3T1IrradTime")
c.execute("DROP TABLE IF EXISTS P4T1IrradTime")

c.execute('''CREATE TABLE PLANTCITY (SiteName TEXT primary key,SiteCity TEXT);''')
conn.execute("INSERT INTO PLANTCITY (SiteName,SiteCity) \
      VALUES ('BatCave','Bulverde')");
conn.execute("INSERT INTO PLANTCITY (SiteName,SiteCity) \
      VALUES ('GreatPlains','Paris')");
conn.execute("INSERT INTO PLANTCITY (SiteName,SiteCity) \
      VALUES ('NW-Vista','Boerne')");
conn.execute("INSERT INTO PLANTCITY (SiteName,SiteCity) \
      VALUES ('RiverBend','FallsCity')");
conn.commit()

c.execute('''CREATE TABLE CITYADDRESS (SiteAddress TEXT primary key,SiteCity TEXT);''')
conn.execute("INSERT INTO CITYADDRESS (SiteAddress,SiteCity) \
      VALUES ('1856ScenicLoop','Bulverde')");
conn.execute("INSERT INTO CITYADDRESS (SiteAddress,SiteCity) \
      VALUES ('5StateHwy1','Paris')");
conn.execute("INSERT INTO CITYADDRESS (SiteAddress,SiteCity) \
      VALUES ('100AeroSt','Boerne')");
conn.execute("INSERT INTO CITYADDRESS (SiteAddress,SiteCity) \
      VALUES ('20987SmithRd.','FallsCity')");
conn.commit()

c.execute('''CREATE TABLE PLANTPANEL (SiteName TEXT,PanelNum Integer);''')
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('BatCave',1)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('BatCave',2)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('BatCave',3)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('BatCave',4)");

conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('GreatPlains',1)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('GreatPlains',2)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('GreatPlains',3)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('GreatPlains',4)");

conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('NW-Vista',1)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('NW-Vista',2)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('NW-Vista',3)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('NW-Vista',4)");

conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('RiverBend',1)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('RiverBend',2)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('RiverBend',3)");
conn.execute("INSERT INTO PLANTPANEL (SiteName,PanelNum) \
      VALUES ('RiverBend',4)");
conn.commit()

c.execute('''CREATE TABLE PANELSENSOR (PanelNum Integer,SensorNum Integer PRIMARY KEY);''')
conn.execute("INSERT INTO PANELSENSOR(PanelNum,SensorNum) \
      VALUES (1,10)");
conn.execute("INSERT INTO PANELSENSOR (PanelNum,SensorNum) \
      VALUES (1,20)");
conn.execute("INSERT INTO PANELSENSOR (PanelNum,SensorNum) \
      VALUES (2,30)");
conn.execute("INSERT INTO PANELSENSOR (PanelNum,SensorNum) \
      VALUES (2,40)");
conn.execute("INSERT INTO PANELSENSOR (PanelNum,SensorNum) \
      VALUES (3,50)");
conn.execute("INSERT INTO PANELSENSOR (PanelNum,SensorNum) \
      VALUES (3,60)");
conn.execute("INSERT INTO PANELSENSOR (PanelNum,SensorNum) \
      VALUES (4,70)");
conn.execute("INSERT INTO PANELSENSOR (PanelNum,SensorNum) \
      VALUES (4,80)");
conn.commit()

#TABLE FOR PLANT 1 DATES
c.execute('''CREATE TABLE P1DATES(SiteName TEXT,Dates TEXT primary key);''')
conn.execute("INSERT INTO P1DATES (SiteName,Dates) \
      VALUES ('BatCave','2000-01-01')");
conn.execute("INSERT INTO P1DATES (SiteName,Dates) \
      VALUES ('BatCave','2000-02-01')");
conn.execute("INSERT INTO P1DATES (SiteName,Dates) \
      VALUES ('BatCave','2000-03-01')");
conn.commit()

#TABLE FOR PLANT 2 DATES
c.execute('''CREATE TABLE P2DATES(SiteName TEXT,Dates TEXT primary key);''')
conn.execute("INSERT INTO P2DATES (SiteName,Dates) \
      VALUES ('GreatPlains','2000-01-01')");
conn.execute("INSERT INTO P2DATES (SiteName,Dates) \
      VALUES ('GreatPlains','2000-02-01')");
conn.execute("INSERT INTO P2DATES (SiteName,Dates) \
      VALUES ('GreatPlains','2000-03-01')");
conn.commit()

#TABLE FOR PLANT 3 DATES
c.execute('''CREATE TABLE P3DATES(SiteName TEXT,Dates TEXT primary key);''')
conn.execute("INSERT INTO P3DATES (SiteName,Dates) \
      VALUES ('NW-Vista','2000-01-01')");
conn.execute("INSERT INTO P3DATES (SiteName,Dates) \
      VALUES ('NW-Vista','2000-02-01')");
conn.execute("INSERT INTO P3DATES (SiteName,Dates) \
      VALUES ('NW-Vista','2000-03-01')");
conn.commit()

#TABLE FOR PLANT 4 DATES
c.execute('''CREATE TABLE P4DATES(SiteName TEXT,Dates TEXT primary key);''')
conn.execute("INSERT INTO P4DATES (SiteName,Dates) \
      VALUES ('RiverBend','2000-01-01')");
conn.execute("INSERT INTO P4DATES (SiteName,Dates) \
      VALUES ('RiverBend','2000-02-01')");
conn.execute("INSERT INTO P4DATES (SiteName,Dates) \
      VALUES ('RiverBend','2000-03-01')");
conn.commit()

####################################################
#PLANTS/DATES/TEMPERAURE TABLES
####################################################
#TABLE FOR PLANT 1 DATE 1 Temperature
tplant=('BatCave',)
c.execute('''CREATE TABLE P1M1TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	#print('{0} , {1}'.format(row[0], row[1]))
	conn.execute("INSERT INTO P1M1TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()
#c.execute('SELECT * FROM P1M1TEMP ORDER BY SensorTemp')
#print c.fetchall()

#TABLE FOR PLANT 1 DATE 2 Temperature
c.execute('''CREATE TABLE P1M2TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P1M2TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()

#TABLE FOR PLANT 1 DATE 3 Temperature
c.execute('''CREATE TABLE P1M3TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P1M3TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()


#TABLE FOR PLANT 2 DATE 1 Temperature
tplant=('GreatPlains',)
c.execute('''CREATE TABLE P2M1TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P2M1TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()

#TABLE FOR PLANT 2 DATE 2 Temperature
c.execute('''CREATE TABLE P2M2TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P2M2TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()

#TABLE FOR PLANT 2 DATE 3 Temperature
c.execute('''CREATE TABLE P2M3TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P2M3TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()


#TABLE FOR PLANT 3 DATE 1 Temperature
tplant=('NW-Vista',)
c.execute('''CREATE TABLE P3M1TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P3M1TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()

#TABLE FOR PLANT 3 DATE 2 Temperature
c.execute('''CREATE TABLE P3M2TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P3M2TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()

#TABLE FOR PLANT 3 DATE 3 Temperature
c.execute('''CREATE TABLE P3M3TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P3M3TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()


#TABLE FOR PLANT 4 DATE 1 Temperature
tplant=('RiverBend',)
c.execute('''CREATE TABLE P4M1TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P4M1TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()

#TABLE FOR PLANT 4 DATE 2 Temperature
c.execute('''CREATE TABLE P4M2TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P4M2TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()

#TABLE FOR PLANT 4 DATE 3 Temperature
c.execute('''CREATE TABLE P4M3TEMP(Dates TEXT,SensorTemp INTEGER);''')
c.execute('SELECT Dates,SensorTemp FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, temptemperature = row
	conn.execute("INSERT INTO P4M3TEMP (Dates,SensorTemp) \
      VALUES (?,?);",(tempdates, temptemperature));
conn.commit()
####################################################
#END - PLANTS/DATES/TEMPERAURE TABLES
####################################################

####################################################
#PLANTS/DATES/IRRADIANCE TABLES
####################################################
#TABLE FOR PLANT 1 DATE 1 irradiance
tplant=('BatCave',)
c.execute('''CREATE TABLE P1M1Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	#print('{0} , {1}'.format(row[0], row[1]))
	conn.execute("INSERT INTO P1M1Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()
#c.execute('SELECT * FROM P1M1Irradiance ORDER BY SensorIrradiance')
#print c.fetchall()

#TABLE FOR PLANT 1 DATE 2 irradiance
c.execute('''CREATE TABLE P1M2Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P1M2Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()

#TABLE FOR PLANT 1 DATE 3 irradiance
c.execute('''CREATE TABLE P1M3Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P1M3Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()


#TABLE FOR PLANT 2 DATE 1 irradiance
tplant=('GreatPlains',)
c.execute('''CREATE TABLE P2M1Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P2M1Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()

#TABLE FOR PLANT 2 DATE 2 irradiance
c.execute('''CREATE TABLE P2M2Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P2M2Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()

#TABLE FOR PLANT 2 DATE 3 irradiance
c.execute('''CREATE TABLE P2M3Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P2M3Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()


#TABLE FOR PLANT 3 DATE 1 irradiance
tplant=('NW-Vista',)
c.execute('''CREATE TABLE P3M1Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P3M1Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()

#TABLE FOR PLANT 3 DATE 2 irradiance
c.execute('''CREATE TABLE P3M2Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P3M2Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()

#TABLE FOR PLANT 3 DATE 3 irradiance
c.execute('''CREATE TABLE P3M3Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P3M3Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()


#TABLE FOR PLANT 4 DATE 1 irradiance
tplant=('RiverBend',)
c.execute('''CREATE TABLE P4M1Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P4M1Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()

#TABLE FOR PLANT 4 DATE 2 irradiance
c.execute('''CREATE TABLE P4M2Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P4M2Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()

#TABLE FOR PLANT 4 DATE 3 irradiance
c.execute('''CREATE TABLE P4M3Irradiance(Dates TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Dates,SensorIrradiance FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradiance = row
	conn.execute("INSERT INTO P4M3Irradiance (Dates,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradiance));
conn.commit()
####################################################
#END - PLANTS/DATES/IRRADIANCE TABLES
####################################################

####################################################
#PLANTS/DATES/IRRADIANCE-TIME TABLES
####################################################
#TABLE FOR PLANT 1 TIME irradiance
tplant=('BatCave',)
c.execute('''CREATE TABLE P1T1IrradTime(Time TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Time,SensorIrradiance FROM solarenergyplant WHERE SiteName=?',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradtime = row
	#print('{0} , {1}'.format(row[0], row[1]))
	conn.execute("INSERT INTO P1T1IrradTime (Time,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradtime));
conn.commit()
#c.execute('SELECT * FROM P1T1IrradTime')
#print c.fetchall()

#TABLE FOR PLANT 2 time irradiance
tplant=('GreatPlains',)
c.execute('''CREATE TABLE P2T1IrradTime(Time TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Time,SensorIrradiance FROM solarenergyplant WHERE SiteName=?',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradtime = row
	#print('{0} , {1}'.format(row[0], row[1]))
	conn.execute("INSERT INTO P2T1IrradTime (Time,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradtime));
conn.commit()
#c.execute('SELECT * FROM P2T1IrradTime')
#print c.fetchall()

#TABLE FOR PLANT 3 time irradiance
tplant=('NW-Vista',)
c.execute('''CREATE TABLE P3T1IrradTime(Time TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Time,SensorIrradiance FROM solarenergyplant WHERE SiteName=?',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradtime = row
	#print('{0} , {1}'.format(row[0], row[1]))
	conn.execute("INSERT INTO P3T1IrradTime (Time,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradtime));
conn.commit()
#c.execute('SELECT * FROM P3T1IrradTime')
#print c.fetchall()

#TABLE FOR PLANT 4 time irradiance
tplant=('RiverBend',)
c.execute('''CREATE TABLE P4T1IrradTime(Time TEXT,SensorIrradiance INTEGER);''')
c.execute('SELECT Time,SensorIrradiance FROM solarenergyplant WHERE SiteName=?',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempirradtime = row
	#print('{0} , {1}'.format(row[0], row[1]))
	conn.execute("INSERT INTO P4T1IrradTime (Time,SensorIrradiance) \
      VALUES (?,?);",(tempdates, tempirradtime));
conn.commit()
#c.execute('SELECT * FROM P4T1IrradTime')
#print c.fetchall()
####################################################
#END - PLANTS/DATES/IRRADIANCE TABLES
####################################################


####################################################
#PLANTS/DATES/WATTS TABLES
####################################################
#TABLE FOR PLANT 1 DATE 1 Watts
tplant=('BatCave',)
c.execute('''CREATE TABLE P1M1Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	#print('{0} , {1}'.format(row[0], row[1]))
	conn.execute("INSERT INTO P1M1Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()
#c.execute('SELECT * FROM P1M1Watts ORDER BY PanelWatts')
#print c.fetchall()

#TABLE FOR PLANT 1 DATE 2 Watts
c.execute('''CREATE TABLE P1M2Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P1M2Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()

#TABLE FOR PLANT 1 DATE 3 Watts
c.execute('''CREATE TABLE P1M3Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P1M3Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()


#TABLE FOR PLANT 2 DATE 1 Watts
tplant=('GreatPlains',)
c.execute('''CREATE TABLE P2M1Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P2M1Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()

#TABLE FOR PLANT 2 DATE 2 Watts
c.execute('''CREATE TABLE P2M2Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P2M2Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()

#TABLE FOR PLANT 2 DATE 3 Watts
c.execute('''CREATE TABLE P2M3Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P2M3Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()


#TABLE FOR PLANT 3 DATE 1 Watts
tplant=('NW-Vista',)
c.execute('''CREATE TABLE P3M1Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P3M1Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()

#TABLE FOR PLANT 3 DATE 2 Watts
c.execute('''CREATE TABLE P3M2Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P3M2Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()

#TABLE FOR PLANT 3 DATE 3 Watts
c.execute('''CREATE TABLE P3M3Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P3M3Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()


#TABLE FOR PLANT 4 DATE 1 Watts
tplant=('RiverBend',)
c.execute('''CREATE TABLE P4M1Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-01-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P4M1Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()

#TABLE FOR PLANT 4 DATE 2 Watts
c.execute('''CREATE TABLE P4M2Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-02-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P4M2Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()

#TABLE FOR PLANT 4 DATE 3 Watts
c.execute('''CREATE TABLE P4M3Watts(Dates TEXT,PanelWatts INTEGER);''')
c.execute('SELECT Dates,PanelWatts FROM solarenergyplant WHERE SiteName=? AND Dates="2000-03-01"',tplant)
all_rows = c.fetchall()
for row in all_rows:
	tempdates, tempWatts = row
	conn.execute("INSERT INTO P4M3Watts (Dates,PanelWatts) \
      VALUES (?,?);",(tempdates, tempWatts));
conn.commit()
####################################################
#END - PLANTS/DATES/WATTS TABLES
####################################################

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())