with open("C:\\Users\\Admin\\Desktop\\cities.bin",'wb') as f:
    n = int(input("How many cities?"))
    record_length = 20   # intializing record length

    for i in range(n):
        city = input("Enter city: ")
        length = len(city)
        city = city + (record_length - length) * ' '
        city = city.encode()
        f.write(city)

with open("C:\\Users\\Admin\\Desktop\\cities.bin",'rb') as f:
    string = f.read()
    print("File details: ",string.decode())
    print("-------------------------------------------")
    no = int(input("Enter record number: "))
    f.seek(record_length * (no-1))
    string = f.read(record_length)
    print(string.decode())

