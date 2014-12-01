import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3

conn = sqlite3.connect('solarenergyplant.db')

c=conn.cursor()
c.execute("DROP TABLE IF EXISTS solarenergyplant")
c.execute('''CREATE TABLE solarenergyplant (SiteName,SiteAddress,SiteCity,PanelNum,PanelWatts,SensorNum,SensorTemp,SensorIrradiance,Dates,Time)''')

text_file=open("GeneralData.txt",'r')
lines = text_file.read().split('\n')
data=[]
#print type(lines)
#print lines.shape
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
#indx=range(1,len(lines)-1)
#print indx
#range(len(lines)-1)
for n in range(1,len(lines)-1):
    data.append(str(lines[n]))
    #print "\n"
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
    c.execute("INSERT INTO solarenergyplant VALUES (?,?,?,?,?,?,?,?,?,?);",(SiteName,SiteAddress,SiteCity,PanelNum,PanelWatts,SensorNum,SensorTemp,SensorIrradiance,Dates,Time))
    conn.commit()
conn.close()    

