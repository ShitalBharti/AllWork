import requests

from database import mydb

url = 'https://gita-api.vercel.app/tel/verse/2/1'
gita_data = requests.get(url).json()
print(gita_data)

# Json Data to store in file
# with open('geetadata.txt','w',encoding="utf-8") as f:
#     for value in gita_data.values():
#         f.write(str(value))

# Json data to store in database
cursor = mydb.cursor(prepared=True)

for key,value in gita_data.items():
    query = "INSERT INTO GitaDetails (Name,description) VALUES (%s, %s)"
    # print(type(key))
    # print(type(value))
    if key == 'purport':
        value = ' '.join(map(str, value))
    cursor.execute(query, (key,value))

mydb.commit()
print("Row Inserted....")

cursor.close()
mydb.close()

#r=requests.get('<MY_URI>', auth=('<YOUR_USERNAME>', '<YOUR_PASSWORD>'))