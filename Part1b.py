import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sqlite3

conn = sqlite3.connect('database.db')
c=conn.cursor()

for row in c.execute('SELECT * FROM solardata'):
	print row