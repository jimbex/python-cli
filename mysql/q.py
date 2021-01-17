import mysql.connector

db3 = mysql.connector.connect(
	host='localhost',
	user='root',
	password='jimbex',
	database='mydatabase')

mycursor = db3.cursor()

mycursor.execute('SELECT * from first WHERE name = "basit"')

myresult = mycursor.fetchall()

for x in myresult:
	print(x)