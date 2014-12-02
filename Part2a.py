#The following code provides the answers for the first question in part 2 by
#Retrieving the information from the previously created data tables on Part1b.py
#Average operation is done outside of the SQL statement for demonstration purposes
#On data extraction and manipulation using python
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3

conn = sqlite3.connect('solarenergyplant.db')
c=conn.cursor()

####################################################
#Average Temperature for Plant 'BatCave'
####################################################
#Temperature Average Computation for Plant BatCave during Month 2000-01-01
c.execute('SELECT SensorTemp FROM P1M1TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
tplant='BatCave' #Plant Name
Dates="2000-01-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant BatCave during Month 2000-02-01
c.execute('SELECT SensorTemp FROM P1M2TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-02-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant BatCave during Month 2000-03-01
c.execute('SELECT SensorTemp FROM P1M3TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-03-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)
####################################################
#End - Average Temperature for Plant 'BatCave'
####################################################

####################################################
#Average Temperature for Plant 'GreatPlains'
####################################################
#Temperature Average Computation for Plant GreatPlains during Month 2000-01-01
c.execute('SELECT SensorTemp FROM P2M1TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
tplant='GreatPlains' #Plant Name
Dates="2000-01-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant GreatPlains during Month 2000-02-01
c.execute('SELECT SensorTemp FROM P2M2TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-02-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant GreatPlains during Month 2000-03-01
c.execute('SELECT SensorTemp FROM P2M3TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-03-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)
####################################################
#End - Average Temperature for Plant 'GreatPlains'
####################################################

####################################################
#Average Temperature for Plant 'NW-Vista'
####################################################
#Temperature Average Computation for Plant NW-Vista during Month 2000-01-01
c.execute('SELECT SensorTemp FROM P3M1TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
tplant='NW-Vista' #Plant Name
Dates="2000-01-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant NW-Vista during Month 2000-02-01
c.execute('SELECT SensorTemp FROM P3M2TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-02-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant NW-Vista during Month 2000-03-01
c.execute('SELECT SensorTemp FROM P3M3TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-03-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)
####################################################
#End - Average Temperature for Plant 'NW-Vista'
####################################################

####################################################
#Average Temperature for Plant 'RiverBend'
####################################################
#Temperature Average Computation for Plant RiverBend during Month 2000-01-01
c.execute('SELECT SensorTemp FROM P4M1TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
tplant='RiverBend' #Plant Name
Dates="2000-01-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant RiverBend during Month 2000-02-01
c.execute('SELECT SensorTemp FROM P4M2TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-02-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)

#Temperature Average Computation for Plant RiverBend during Month 2000-03-01
c.execute('SELECT SensorTemp FROM P4M3TEMP') #Retrieve Temperature from Table
all_rows = c.fetchall() #Get Values from Table
numelements=0 #Initialize Values
temperaturesum=0 #Initialize Values
for row in all_rows:
	temptemperature = int(''.join(map(str,row)))
	temperaturesum=temperaturesum+temptemperature #Add Temperature Values
	numelements=numelements+1 #Add Increment
Dates="2000-03-01" #Current Date
temperatureavg=float(temperaturesum)/float(numelements) #Average Calculation
print "The Average temperature for Plant %s during Month %s is: %f" %(tplant,Dates,temperatureavg)
####################################################
#End - Average Temperature for Plant 'RiverBend'
####################################################
conn.close()