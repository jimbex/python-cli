import re
file = open('dump1.txt', 'r')
files = file.read()
data = []

fil = re.findall('[A-Za-z]+\S:', files)

for i in fil:
    data.append(i)
    
b = []
for x in data:
    b.append(x[0:-1])

