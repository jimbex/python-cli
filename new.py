import re

num = []

file = open('regex_sum.txt', 'r')
rid = file.read()

b = re.findall('[0-9]+', rid)

for x in b:
	x = int(x)
	num.append(x)

print(sum(num))