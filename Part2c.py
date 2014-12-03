#The following code provides the answers for the third question in part 2 by
#Retrieving the information from the previously created data tables on Part1b.py
#Sum operation is done inside of the SQL statement for demonstration purposes

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3

conn = sqlite3.connect('solarenergyplant.db')
c=conn.cursor()

####################################################
#Total Wattage per Month for Plant 'BatCave'
####################################################
P1twattage=[] #Total Wattage Collector
P1Months=[] #Month Collector
#Total Watts for Plant BatCave during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P1M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='BatCave' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P1twattage.append(tempwatts) #Total Wattage Collector
P1Months.append(Dates) #Month Collector

#Total Watts for Plant BatCave during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P1M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='BatCave' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P1twattage.append(tempwatts) #Total Wattage Collector
P1Months.append(Dates) #Month Collector

#Total Watts for Plant BatCave during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P1M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='BatCave' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P1twattage.append(tempwatts) #Total Wattage Collector
P1Months.append(Dates) #Month Collector
####################################################
#END - Total Wattage per Month for Plant 'BatCave'
####################################################
#print P1twattage #Total Wattage Collector
#print P1Months #Month Collector
####################################################
#Total Wattage per Month for Plant 'GreatPlains'
####################################################
P2twattage=[] #Total Wattage Collector
P2Months=[] #Month Collector
#Total Watts for Plant GreatPlains during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P2M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='GreatPlains' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P2twattage.append(tempwatts) #Total Wattage Collector
P2Months.append(Dates) #Month Collector

#Total Watts for Plant GreatPlains during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P2M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='GreatPlains' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P2twattage.append(tempwatts) #Total Wattage Collector
P2Months.append(Dates) #Month Collector

#Total Watts for Plant GreatPlains during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P2M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='GreatPlains' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P2twattage.append(tempwatts) #Total Wattage Collector
P2Months.append(Dates) #Month Collector
####################################################
#END - Total Wattage per Month for Plant 'GreatPlains'
####################################################
#print P2twattage #Total Wattage Collector
#print P2Months #Month Collector
####################################################
#Total Wattage per Month for Plant 'NW-Vista'
####################################################
P3twattage=[] #Total Wattage Collector
P3Months=[] #Month Collector
#Total Watts for Plant NW-Vista during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P3M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='NW-Vista' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P3twattage.append(tempwatts) #Total Wattage Collector
P3Months.append(Dates) #Month Collector

#Total Watts for Plant NW-Vista during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P3M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='NW-Vista' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P3twattage.append(tempwatts) #Total Wattage Collector
P3Months.append(Dates) #Month Collector

#Total Watts for Plant NW-Vista during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P3M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='NW-Vista' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P3twattage.append(tempwatts) #Total Wattage Collector
P3Months.append(Dates) #Month Collector
####################################################
#END - Total Wattage per Month for Plant 'NW-Vista'
####################################################
#print P3twattage #Total Wattage Collector
#print P3Months #Month Collector
####################################################
#Total Wattage per Month for Plant 'RiverBend'
####################################################
P4twattage=[] #Total Wattage Collector
P4Months=[] #Month Collector
#Total Watts for Plant RiverBend during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P4M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='RiverBend' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P4twattage.append(tempwatts) #Total Wattage Collector
P4Months.append(Dates) #Month Collector

#Total Watts for Plant RiverBend during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P4M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='RiverBend' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P4twattage.append(tempwatts) #Total Wattage Collector
P4Months.append(Dates) #Month Collector

#Total Watts for Plant RiverBend during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P4M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='RiverBend' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
P4twattage.append(tempwatts) #Total Wattage Collector
P4Months.append(Dates) #Month Collector
####################################################
#END - Total Wattage per Month for Plant 'RiverBend'
####################################################
#print P4twattage #Total Wattage Collector
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
rects1 = ax.bar(ind, P1twattage, width, color='b')
rects2 = ax.bar(ind+3, P2twattage, width, color='g')
rects3 = ax.bar(ind+6, P3twattage, width, color='y')
rects4 = ax.bar(ind+9, P4twattage, width, color='r')

#Add X and Y Axis labels and Title
ax.set_ylabel('Total Wattage')
ax.set_title('Tottal Wattage per Plant and Month')
ax.set_xticks(ind2)
ax.set_xticklabels(Tmonths, rotation=45)

#Define Legend
ax.legend( (rects1[0],rects2[0],rects3[0],rects4[0]), ('BatCave','GreatPlains','NW-Vista','RiverBend') ,loc=4)
plt.axis([0, 12, 0, 2000])

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