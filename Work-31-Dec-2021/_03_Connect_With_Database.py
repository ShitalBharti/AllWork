import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database = "pythonDB",    # give database name
  user="root",
  password="root"
)

print(mydb)