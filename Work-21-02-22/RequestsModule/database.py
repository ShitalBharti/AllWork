import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database = "pythonDB",    # give database name
  user="root",
  password="root"
)

print(mydb)
# cursor = mydb.cursor()
#
#  # query = "create table GitaDetails(chapter_no int,verse_no int,language varchar(100),chapter_name varchar(100)," \
#  #        "verse varchar(100),transliteration varchar(100), synonyms varchar(1000),audio_link text, " \
#  #        "translation text,purport text )"
#
# query = "create table GitaDetails(Name varchar(20), description text)"
#
# cursor.execute(query)
#
# mydb.commit()
# print("Table Created....")
#
# cursor.close()
# mydb.close()