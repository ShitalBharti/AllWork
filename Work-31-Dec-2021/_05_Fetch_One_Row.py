import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database = "pythonDB",
  user="root",
  password="root"
)

cursor = mydb.cursor()

cursor.execute("Select * from empinfo")

row = cursor.fetchone()
while row is not None:
    print(row)          # display it
    row = cursor.fetchone() # get the next one

cursor.close()
mydb.close()



