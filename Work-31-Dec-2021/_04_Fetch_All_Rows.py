import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",         # in the network server, ip address is given but if we use individual computer, then string localhost can be supplied.
  database = "pythonDB",    # give database name
  user="root",              # Mysql username
  password="root"           # Mysql password
)

cursor = mydb.cursor()      # cursor class object using cursor() method

"""
cursor object is useful to execute SQL commands on the database. For this purpose, we can use execute() method of 'cursor' object.
"""

cursor.execute("Select * from empinfo") # mysql query using execute() method

rows = cursor.fetchall()

print(type(rows))         # type is list
print("Total no. of rows are = ",cursor.rowcount)

for row in rows:
  print(row)

# close connection
cursor.close()
mydb.close()



