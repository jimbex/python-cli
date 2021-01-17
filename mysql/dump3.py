import mysql.connector
import re
import sqlite3

conn = sqlite3.connect('dump.sqlite')
cur = conn.cursor()
file = open('dump1.txt', 'r')
files = file.read()
data = []

fil = re.findall(': .+', files)

for i in fil:
    data.append(i)
    
b = []
for x in data:
    b.append(x[2:])


for x in b:
	cur.execute('INSERT INTO First(value) VALUES(?)', (x,))

conn.commit()
cur.close()