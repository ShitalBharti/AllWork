import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database = "pythonDB",
  user="root",
  password="root"
)

cursor = mydb.cursor()

query = "insert into empinfo values(2,'Vitthal',550000.70)"

cursor.execute(query)

mydb.commit()
print("1 row inserted....")

cursor.close()
mydb.close()
