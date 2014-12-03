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
P1maxirrad=[] #Max Irradiance Collector
P1Months=[] #Month Collector
P1time=[] #Time Collector
#Max Irradiance for Plant BatCave with Corresponding Date(2000-01-01) and Time
tplant='BatCave' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P1M1Irradiance x INNER JOIN P1T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P1maxirrad.append(tempirrad1) #Max Irradiance Collector
P1Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P1time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector

#Max Irradiance for Plant BatCave with Corresponding Date(2000-02-01) and Time
tplant='BatCave' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P1M2Irradiance x INNER JOIN P1T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P1maxirrad.append(tempirrad1) #Max Irradiance Collector
P1Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P1time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector

#Max Irradiance for Plant BatCave with Corresponding Date(2000-03-01) and Time
tplant='BatCave' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P1M3Irradiance x INNER JOIN P1T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P1maxirrad.append(tempirrad1) #Max Irradiance Collector
P1Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P1time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'BatCave'
####################################################################
#print P1maxirrad #Max Irradiance Collector
#print P1Months #Month Collector
#print P1time #Time Collector
####################################################################
#Maximum Irradiance per Plant per Month for Plant 'GreatPlains'
####################################################################
P2maxirrad=[] #Max Irradiance Collector
P2Months=[] #Month Collector
P2time=[] #Time Collector
#Max Irradiance for Plant GreatPlains with Corresponding Date(2000-01-01) and Time
tplant='GreatPlains' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P2M1Irradiance x INNER JOIN P2T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P2maxirrad.append(tempirrad1) #Max Irradiance Collector
P2Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P2time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector

#Max Irradiance for Plant GreatPlains with Corresponding Date(2000-02-01) and Time
tplant='GreatPlains' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P2M2Irradiance x INNER JOIN P2T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P2maxirrad.append(tempirrad1) #Max Irradiance Collector
P2Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P2time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector

#Max Irradiance for Plant GreatPlains with Corresponding Date(2000-03-01) and Time
tplant='GreatPlains' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P2M3Irradiance x INNER JOIN P2T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P2maxirrad.append(tempirrad1) #Max Irradiance Collector
P2Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P2time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'GreatPlains'
####################################################################
#print P2maxirrad #Max Irradiance Collector
#print P2Months #Month Collector
#print P2time #Time Collector
####################################################################
#Maximum Irradiance per Plant per Month for Plant 'NW-Vista'
####################################################################
P3maxirrad=[] #Max Irradiance Collector
P3Months=[] #Month Collector
P3time=[] #Time Collector
#Max Irradiance for Plant NW-Vista with Corresponding Date(2000-01-01) and Time
tplant='NW-Vista' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P3M1Irradiance x INNER JOIN P3T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P3maxirrad.append(tempirrad1) #Max Irradiance Collector
P3Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P3time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector

#Max Irradiance for Plant NW-Vista with Corresponding Date(2000-02-01) and Time
tplant='NW-Vista' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P3M2Irradiance x INNER JOIN P3T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P3maxirrad.append(tempirrad1) #Max Irradiance Collector
P3Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P3time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector

#Max Irradiance for Plant NW-Vista with Corresponding Date(2000-03-01) and Time
tplant='NW-Vista' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P3M3Irradiance x INNER JOIN P3T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P3maxirrad.append(tempirrad1) #Max Irradiance Collector
P3Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P3time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'NW-Vista'
####################################################################
#print P3maxirrad #Max Irradiance Collector
#print P3Months #Month Collector
#print P3time #Time Collector
####################################################################
#Maximum Irradiance per Plant per Month for Plant 'RiverBend'
####################################################################
P4maxirrad=[] #Max Irradiance Collector
P4Months=[] #Month Collector
P4time=[] #Time Collector
#Max Irradiance for Plant RiverBend with Corresponding Date(2000-01-01) and Time
tplant='RiverBend' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P4M1Irradiance x INNER JOIN P4T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P4maxirrad.append(tempirrad1) #Max Irradiance Collector
P4Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P4time.append(str(''.join(map(str,temptime))).rstrip())#Time Collector

#Max Irradiance for Plant RiverBend with Corresponding Date(2000-02-01) and Time
tplant='RiverBend' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P4M2Irradiance x INNER JOIN P4T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P4maxirrad.append(tempirrad1) #Max Irradiance Collector
P4Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P4time.append(str(''.join(map(str,temptime))).rstrip()) #Time Collector

#Max Irradiance for Plant RiverBend with Corresponding Date(2000-03-01) and Time
tplant='RiverBend' #Plant Name
#Retrieve Date,Irradiance and Time from Inner Joined Tables
c.execute('SELECT x.Dates,MAX(x.SensorIrradiance), y.Time, y.SensorIrradiance FROM P4M3Irradiance x INNER JOIN P4T1IrradTime y WHERE x.SensorIrradiance=y.SensorIrradiance')
all_rows = c.fetchall() #Get Values from Table
for row in all_rows:
	tempdates,tempirrad1,temptime,tempirrad2 = row
print "The Maximum Irradiance for Plant %s during Month %s is: %i measured at time: %s" %(tplant,tempdates,tempirrad1,temptime)
P4maxirrad.append(tempirrad1) #Max Irradiance Collector
P4Months.append(str(''.join(map(str,tempdates)))) #Month Collector
P4time.append(str(''.join(map(str,temptime))).rstrip()) #Time Collector
####################################################################
#END - Maximum Irradiance per Plant per Month for Plant 'RiverBend'
####################################################################
#print P4maxirrad #Max Irradiance Collector
#print P4Months #Month Collector
#print P4time #Time Collector
conn.close()

####################################################
#PLOT
####################################################
Tmonths=P1Months+P2Months+P3Months+P4Months
Ttime=P1time+P2time+P3time+P4time
N = 3 #Bars per Plant
N2= 12 #Total X Labels
ind = np.arange(N) #Bars per Plant
ind2= np.arange(N2) #Total X Labels
width = 0.5 #Bar width

fig, ax = plt.subplots()
rects1 = ax.bar(ind, P1maxirrad, width, color='b')
rects2 = ax.bar(ind+3, P2maxirrad, width, color='g')
rects3 = ax.bar(ind+6, P3maxirrad, width, color='y')
rects4 = ax.bar(ind+9, P4maxirrad, width, color='r')

#Add X and Y Axis labels and Title
ax.set_ylabel('Max Irradiance')
ax.set_title('Max Irradiance per Plant and Month - (All foud at 12:00 Hrs)')
ax.set_xticks(ind2)
ax.set_xticklabels(Tmonths, rotation=45)

#Define Legend
ax.legend( (rects1[0],rects2[0],rects3[0],rects4[0]), ('BatCave','GreatPlains','NW-Vista','RiverBend') ,loc=4)
plt.axis([0, 12, 0, 80])

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