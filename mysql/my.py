import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="basit",
  password="jimbex",
  database="mydatabase"
)


mycursor = mydb.cursor()

mycursor.execute("INSERT INTO test(username, pass) VALUES ('farouk', 'jimbex')")


mydb.commit()