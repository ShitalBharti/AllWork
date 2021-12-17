"""
-> Memory mapped file is a module in python that is useful to map or link to a binary file and manipulate the data of the file as we do with strings.
-> If binary file is created with some data, data is viewed as strings and can be manipulated using mmap module.
"""
# program to create phone book with names and phone numbers

with open('C:\\Users\\Admin\\Desktop\\phonebook.dat','wb') as f:
    n = int(input("How many entries? "))
    for i in range(n):
        name = input("Enter Name:")
        phone = input("Enter Phone No:")
        name = name.encode()
        phone = phone.encode()
        f.write(name + phone)