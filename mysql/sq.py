import mysql.connector

while True:
	name = input("Enter ur name: ")
	age = input('Enter ur age: ')
	if name == "done":
		break


	db4 = mysql.connector.connect(
		host='localhost',
		user='root',
		password='jimbex',
		database='mydatabase')

	mycursor = db4.cursor()

	ins = 'INSERT INTO first(name, age) VALUES (%s, %s)'
	val = (name, age)

	mycursor.execute(ins, val)
	db4.commit()


mycursor.execute('SELECT * FROM first')
myresult = mycursor.fetchall()
for x in result:
	print(x)