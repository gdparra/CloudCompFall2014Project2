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
#Total Watts for Plant BatCave during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P1M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='BatCave' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant BatCave during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P1M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='BatCave' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant BatCave during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P1M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='BatCave' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
####################################################
#END - Total Wattage per Month for Plant 'BatCave'
####################################################

####################################################
#Total Wattage per Month for Plant 'GreatPlains'
####################################################
#Total Watts for Plant GreatPlains during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P2M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='GreatPlains' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant GreatPlains during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P2M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='GreatPlains' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant GreatPlains during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P2M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='GreatPlains' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
####################################################
#END - Total Wattage per Month for Plant 'GreatPlains'
####################################################

####################################################
#Total Wattage per Month for Plant 'NW-Vista'
####################################################
#Total Watts for Plant NW-Vista during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P3M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='NW-Vista' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant NW-Vista during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P3M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='NW-Vista' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant NW-Vista during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P3M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='NW-Vista' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
####################################################
#END - Total Wattage per Month for Plant 'NW-Vista'
####################################################

####################################################
#Total Wattage per Month for Plant 'RiverBend'
####################################################
#Total Watts for Plant RiverBend during Month 2000-01-01
c.execute('SELECT sum(PanelWatts) FROM P4M1Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='RiverBend' #Plant Name
Dates="2000-01-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant RiverBend during Month 2000-02-01
c.execute('SELECT sum(PanelWatts) FROM P4M2Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='RiverBend' #Plant Name
Dates="2000-02-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)

#Total Watts for Plant RiverBend during Month 2000-03-01
c.execute('SELECT sum(PanelWatts) FROM P4M3Watts') #Retrieve the Sum of Watts from Table
all_rows = c.fetchall() #Get Values from Table
tempwatts = int(''.join(map(str,all_rows[0])))
tplant='RiverBend' #Plant Name
Dates="2000-03-01" #Current Date
print "The total Wattage for Plant %s during Month %s is: %i" %(tplant,Dates,tempwatts)
####################################################
#END - Total Wattage per Month for Plant 'RiverBend'
####################################################
conn.close()