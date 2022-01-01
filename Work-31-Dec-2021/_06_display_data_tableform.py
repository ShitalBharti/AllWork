import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database = "pythonDB",
  user="root",
  password="root"
)

cursor = mydb.cursor()

cursor.execute("Select * from empinfo") # mysql query using execute() method

rows = cursor.fetchall()

print("Total no. of rows are = ",cursor.rowcount)

for row in rows:
    eno = row[0]
    ename = row[1]
    sal = row[2]
    print('eno-------------ename-------------sal')
    print('{}              {}         {}'.format(eno,ename,sal))

# close connection
cursor.close()
mydb.close()



