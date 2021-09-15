import mysql.connector

mydb = mysql.connector.connect(
	hpst="localhost",
	user="root",
	password="password123",
	database="customers_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x  in myresult():
	print(x)