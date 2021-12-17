import os

# searching city name in file

record_length = 20

# find size of file
size = os.path.getsize('C:\\Users\\Admin\\Desktop\\cities.bin')
print('Size of file = {} bytes'.format(size))  # 4 records are in file at current i.e record_length * 4 = 20 * 4 = 80 bytes

# no of records in file
no = int(size/record_length)
print('No of records = {}'.format(no))

# open binary file to read
with open('C:\\Users\\Admin\\Desktop\\cities.bin','rb') as f:
    name = input("Enter City name to find:")
    name = name.encode()

# position represents position of file pointer
    position = 0

# found becomes true if city is found
    found = False

# loop through file to search given name
    for i in range(no):
        f.seek(position)
        string = f.read(20)
        if name in string:
            print("City found at record no:{}".format(i+1))
            found = True
        position += record_length
    if not found:
        print("City not found")