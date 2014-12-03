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
P1avgTemp=[] #Average Temperature Collector
P1Months=[] #Month Collector
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
P1avgTemp.append(temperatureavg) #Average Temperature Collector
P1Months.append(Dates) #Month Collector

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
P1avgTemp.append(temperatureavg) #Average Temperature Collector
P1Months.append(Dates) #Month Collector

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
P1avgTemp.append(temperatureavg) #Average Temperature Collector
P1Months.append(Dates) #Month Collector
####################################################
#End - Average Temperature for Plant 'BatCave'
####################################################
#print P1avgTemp #Average Temperature Collector
#print P1Months #Month Collector
####################################################
#Average Temperature for Plant 'GreatPlains'
####################################################
P2avgTemp=[] #Average Temperature Collector
P2Months=[] #Month Collector
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
P2avgTemp.append(temperatureavg) #Average Temperature Collector
P2Months.append(Dates) #Month Collector

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
P2avgTemp.append(temperatureavg) #Average Temperature Collector
P2Months.append(Dates) #Month Collector

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
P2avgTemp.append(temperatureavg) #Average Temperature Collector
P2Months.append(Dates) #Month Collector
####################################################
#End - Average Temperature for Plant 'GreatPlains'
####################################################
#print P2avgTemp #Average Temperature Collector
#print P2Months #Month Collector
####################################################
#Average Temperature for Plant 'NW-Vista'
####################################################
P3avgTemp=[] #Average Temperature Collector
P3Months=[] #Month Collector
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
P3avgTemp.append(temperatureavg) #Average Temperature Collector
P3Months.append(Dates) #Month Collector

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
P3avgTemp.append(temperatureavg) #Average Temperature Collector
P3Months.append(Dates) #Month Collector

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
P3avgTemp.append(temperatureavg) #Average Temperature Collector
P3Months.append(Dates) #Month Collector
####################################################
#End - Average Temperature for Plant 'NW-Vista'
####################################################
#print P3avgTemp #Average Temperature Collector
#print P3Months #Month Collector
####################################################
#Average Temperature for Plant 'RiverBend'
####################################################
P4avgTemp=[] #Average Temperature Collector
P4Months=[] #Month Collector
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
P4avgTemp.append(temperatureavg) #Average Temperature Collector
P4Months.append(Dates) #Month Collector

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
P4avgTemp.append(temperatureavg) #Average Temperature Collector
P4Months.append(Dates) #Month Collector

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
P4avgTemp.append(temperatureavg) #Average Temperature Collector
P4Months.append(Dates) #Month Collector
####################################################
#End - Average Temperature for Plant 'RiverBend'
####################################################
#print P4avgTemp #Average Temperature Collector
#print P4Months #Month Collector
conn.close()

####################################################
#PLOT
####################################################
Tmonths=P1Months+P2Months+P3Months+P4Months
N = 3 #Bars per Plant
N2= 12 #Total X Labels
ind = np.arange(N) #Bars per Plant
ind2= np.arange(N2) #Total X Labels
width = 0.5 #Bar width

fig, ax = plt.subplots()
rects1 = ax.bar(ind, P1avgTemp, width, color='b')
rects2 = ax.bar(ind+3, P2avgTemp, width, color='g')
rects3 = ax.bar(ind+6, P3avgTemp, width, color='y')
rects4 = ax.bar(ind+9, P4avgTemp, width, color='r')

#Add X and Y Axis labels and Title
ax.set_ylabel('Average Temperature')
ax.set_title('Average Temperature per Plant and Month')
ax.set_xticks(ind2)
ax.set_xticklabels(Tmonths, rotation=45)

#Define Legend
ax.legend( (rects1[0],rects2[0],rects3[0],rects4[0]), ('BatCave','GreatPlains','NW-Vista','RiverBend') ,loc=4)
plt.axis([0, 12, 0, 75])

#Define Bar Labels
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
plt.show()
####################################################
#END - PLOT
####################################################