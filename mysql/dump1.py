import mysql.connector
import re
import sqlite3

conn = sqlite3.connect('mump.sqlite')
cur = conn.cursor()
file = open('dump1.txt', 'r')
files = file.read()
data = []
dat = []

cur.execute('CREATE TABLE IF NOT EXISTS Second(head TEXT, Value TEXT)')

fil = re.findall('[A-Za-z]+\S:', files)

for i in fil:
    data.append(i)
    
b = []
for x in data:
    b.append(x[0:-1])

fill = re.findall(': .+', files)

for i in fill:
    dat.append(i)
    
c = []
for x in dat:
    c.append(x[2:])

n = 0
for x in range(len(data)):
	x = b[n]
	y = c[n]
	cur.execute('INSERT INTO Second(head, value) VALUES(?, ?)', (x, y))
	n+=1

conn.commit()
cur.close()

