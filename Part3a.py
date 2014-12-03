import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3
import csv

#The following section represents the Mapper
text_file=open("solardata.csv",'r') #Document with data of SolarData
file = open('solardata.csv')
reader = csv.reader(file)
next(reader, None)
dailysamps=24 #Number of Samples per day

#Required variabes
day=[] #Daily date list
etr=[] #Daily ETR list
aetr=[] #Average ETR
detr=[]  #Temporal Average ETR
daylist=[] #Final Day List

#Read lines and store day and ETR value in corresponding lists
for line in reader:
	day.append(str(line[0]))
	etr.append(int(line[4]))

#The following section represents the Reducer which will provide the average
for hours in range(0, len(etr),dailysamps):
	detr=np.average(etr[hours:hours+dailysamps])
	aetr.append(detr)
	daylist.append(day[hours])
print aetr
print daylist

####################################################
#PLOT
####################################################
N = len(aetr) #Total Bars
ind = np.arange(N) #Index per Bar
width = 0.5 #Bar width

fig, ax = plt.subplots()
rects1 = ax.bar(ind, aetr, width, color='r')

#Add X and Y Axis labels and Title
ax.set_ylabel('ETR Average')
ax.set_title('Average ETR per Day')
ax.set_xticks(ind)
ax.set_xticklabels(daylist, rotation=45)
plt.axis([0, N+1, 0, 500])

#Define Bar Labels
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
#autolabel(rects1)
plt.show()
####################################################
#END - PLOT
####################################################