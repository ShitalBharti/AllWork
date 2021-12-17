import os

record_length = 20
size = os.path.getsize('C:\\Users\\Admin\\Desktop\\cities.bin')
no = int(size/record_length)

f1 = open('C:\\Users\\Admin\\Desktop\\cities.bin','rb')
f2 = open('C:\\Users\\Admin\\Desktop\\cities.bin','wb')

city = input("Enter city name to delete:")

ln = len(city)
city = city + (record_length - ln) * ' '
city = city.encode()

for i in range(no):
    string = f1.read(record_length)
    if(string != city):
        f2.write(string)
        print("Record deleted!")
        break
f1.close()
f2.close()

# delete total file
os.remove("C:\\Users\\Admin\\Desktop\\cities.bin")

# rename file
os.rename('somefile.bin','C:\\Users\\Admin\\Desktop\\cities.bin')




