import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@61",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name varchar(255), address varchar(255))")