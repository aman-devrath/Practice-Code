import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@61",
    database="mydatabase"
)

mycursor = mydb.cursor()
''' select all'''
# mycursor.execute("SELECT * FROM customers")

''' select where '''
#no security against SQL INJECTION
#mycursor.execute("SELECT * FROM customers where address = 'Highway 21'")

#provides security against SQL INJECTION
sql = "SELECT * FROM customers where address = %s"
val = ("Highway 21",)
mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)