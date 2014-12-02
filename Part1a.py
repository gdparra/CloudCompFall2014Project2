#The following code extracts data from the text document, creates the database solarenergyplant.db,
#Crates the table solarenergyplant where all the data from the text document is goint to be added

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3

conn = sqlite3.connect('solarenergyplant.db')
c=conn.cursor()
c.execute("DROP TABLE IF EXISTS solarenergyplant")
c.execute('''CREATE TABLE solarenergyplant (SiteName,SiteAddress,SiteCity,PanelNum,PanelWatts,SensorNum,SensorTemp,SensorIrradiance,Dates,Time)''')

text_file=open("GeneralData.txt",'r') #Document with data of SolarEnergyPlant
lines = text_file.read().split('\n')

#Initialize Arrays where the data is going to be temporarly allocated
data=[]
SiteName=[]
SiteAddress=[]
SiteCity=[]
PanelNum=[]
PanelWatts=[]
SensorNum=[]
SensorTemp=[]
SensorIrradiance=[]
Dates=[]
Time=[]

#Read each line of information retrieved from the text document
for n in range(1,len(lines)-1):
    data.append(str(lines[n]))
    print n
    print data[n-1]
    print type(data[n-1])
    data2=data[n-1].split(",")
    SiteName=data2[0]
    print SiteName
    print type(SiteName)
    SiteAddress=data2[1]
    print SiteAddress
    print type(SiteAddress)
    SiteCity=data2[2]
    print SiteCity
    print type(SiteCity)
    PanelNum=int(data2[3])
    print PanelNum
    print type(PanelNum)
    PanelWatts=int(data2[4])
    print PanelWatts
    print type(PanelWatts)
    SensorNum=int(data2[5])
    print SensorNum
    print type(SensorNum)
    SensorTemp=int(data2[6])
    print SensorTemp
    print type(SensorTemp)
    SensorIrradiance=int(data2[7])
    print SensorIrradiance
    print type(SensorIrradiance)
    Dates=data2[8]
    print Dates
    print type(Dates)
    Time=data2[9]
    print Time
    print type(Time)

    #Place each data dield into its corresponding place on the created table.
    c.execute("INSERT INTO solarenergyplant VALUES (?,?,?,?,?,?,?,?,?,?);",(SiteName,SiteAddress,SiteCity,PanelNum,PanelWatts,SensorNum,SensorTemp,SensorIrradiance,Dates,Time))
    conn.commit()
conn.close()    

