import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database = "pythonDB",
  user="root",
  password="root"
)

cursor = mydb.cursor()

query = "insert into empinfo values(3,'Akash',600000)"

try:
    cursor.execute(query)
    mydb.commit()               # save the changes to database
    print("1 row inserted....")
except:
    mydb.rollback()             # rollback if there is any error/exception
finally:
    cursor.close()
    mydb.close()