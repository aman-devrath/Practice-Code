import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@61",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES;")

for x in mycursor:
    print(x)