import mysql.connector


db2 = mysql.connector.connect(
  host = "localhost",
  user = 'root',
  password = 'jimbex',
  database = 'mydatabase',
)

mycursor = db2.cursor()

ins = "INSERT INTO first(name, age) VALUES (%s, %s)"
val = ("fareedat", 14)

mycursor.execute(ins, val)

db2.commit()

print(mycursor.rowcount, "was inserted")
print("1 record inserted, ID:", mycursor.lastrowid)



