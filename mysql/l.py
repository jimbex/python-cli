import mysql.connector

db4 = mysql.connector.connect(
	host='localhost',
	user='root',
	password='jimbex',
	database='mydatabase')

mycursor = db4.cursor()

mycursor.execute('DELETE FROM first where id = 2')
db4.commit()
mycursor.execute('SELECT * FROM first')

myresult = mycursor.fetchall()
db4.commit()

for x in myresult:
	print(x)
