import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "jimbex",
	database = "mydatabase")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM test")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)