#The following code provides the answers for the second question in part 2 by
#Inner Joining and retrieving the information from the previously created data tables on Part1b.py
#Max operation is done inside of the SQL statement for demonstration purposes

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3

conn = sqlite3.connect('solarenergyplant.db')
c=conn.cursor()

####################################################################
#Maximum Irradiance per Plant per Month for Plant 'BatCave'
####################################################################
#Max Irradiance for Plant BatCave with Corresponding Date(2000-01-01) and Time
tplant='BatCave' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P1M1Irradiance x INNER JOIN P1T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant BatCave with Corresponding Date(2000-02-01) and Time
tplant='BatCave' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P1M2Irradiance x INNER JOIN P1T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant BatCave with Corresponding Date(2000-03-01) and Time
tplant='BatCave' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P1M3Irradiance x INNER JOIN P1T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'BatCave'
####################################################################

####################################################################
#Maximum Irradiance per Plant per Month for Plant 'GreatPlains'
####################################################################
#Max Irradiance for Plant GreatPlains with Corresponding Date(2000-01-01) and Time
tplant='GreatPlains' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P2M1Irradiance x INNER JOIN P2T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant GreatPlains with Corresponding Date(2000-02-01) and Time
tplant='GreatPlains' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P2M2Irradiance x INNER JOIN P2T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant GreatPlains with Corresponding Date(2000-03-01) and Time
tplant='GreatPlains' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P2M3Irradiance x INNER JOIN P2T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'GreatPlains'
####################################################################

####################################################################
#Maximum Irradiance per Plant per Month for Plant 'NW-Vista'
####################################################################
#Max Irradiance for Plant NW-Vista with Corresponding Date(2000-01-01) and Time
tplant='NW-Vista' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P3M1Irradiance x INNER JOIN P3T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant NW-Vista with Corresponding Date(2000-02-01) and Time
tplant='NW-Vista' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P3M2Irradiance x INNER JOIN P3T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant NW-Vista with Corresponding Date(2000-03-01) and Time
tplant='NW-Vista' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P3M3Irradiance x INNER JOIN P3T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'NW-Vista'
####################################################################

####################################################################
#Maximum Irradiance per Plant per Month for Plant 'RiverBend'
####################################################################
#Max Irradiance for Plant RiverBend with Corresponding Date(2000-01-01) and Time
tplant='RiverBend' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P4M1Irradiance x INNER JOIN P4T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant RiverBend with Corresponding Date(2000-02-01) and Time
tplant='RiverBend' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P4M2Irradiance x INNER JOIN P4T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)

#Max Irradiance for Plant RiverBend with Corresponding Date(2000-03-01) and Time
tplant='RiverBend' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P4M3Irradiance x INNER JOIN P4T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'RiverBend'
####################################################################
conn.close()