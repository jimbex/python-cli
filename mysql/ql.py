import mysql.connector


name = input('Enter username: ')
password = input('Enter password: ')
print('\n')


db = mysql.connector.connect(
	host='localhost',
	user='root',
	password='jimbex',
	database='mydatabase')

mycursor= db.cursor()

mycursor.execute('SELECT username, pass FROM test')

myresult = mycursor.fetchall()

for x, y in myresult:
	if name == x and password == y:
		print('welcome')
		break
	else:
		print('invalid')
		continue



	


