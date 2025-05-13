import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@61",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name,address) VALUES (%s, %s)"
val_single = ("Tyler","Highway 22")

#use execute to insert single value
mycursor.execute(sql,val_single)
mydb.commit()

print(mycursor.rowcount, "records inserted successfully")

val_mult = [
    ("Michael","Highway 23"),
    ("Joe","Highway 24"),
    ("Blake","Highway 25"),
    ("Philip","Highway 26")
]

#use executemany to insert multiple values
mycursor.executemany(sql,val_mult)
mydb.commit()

print(mycursor.rowcount, "records inserted successfully")