import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@61",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

mycursor.execute("DESCRIBE customers")

for row in mycursor:
    print(row)