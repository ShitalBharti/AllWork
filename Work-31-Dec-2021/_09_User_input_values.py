import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database = "pythonDB",
  user="root",
  password="root"
)

cursor = mydb.cursor()

eid = int(input("Enter eid: "))
ename = input("Enter ename: ")
sal= float(input("Enter salary: "))

query = "insert into empinfo values('%d','%s','%f')"

args = (eid, ename, sal)

try:
    cursor.execute(query % args)
    mydb.commit()               # save the changes to database
    print("1 row inserted....")
except:
    mydb.rollback()             # rollback if there is any error/exception
finally:
    cursor.close()
    mydb.close()