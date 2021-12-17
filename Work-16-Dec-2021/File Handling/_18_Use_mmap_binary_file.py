import mmap, sys

print("1 to display all entries")
print("2 to display phone no")
print("3 to modify an entry")
print("4 to exit")

ch = input("Enter you choice..")
if ch == '4':
    sys.exit()

with open('C:\\Users\\Admin\\Desktop\\phonebook.dat', 'r+b') as f:

    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)

    # display the entire file
    if ch == '1':
        print(mm.read().decode())

    # display phone no
    if ch == '2':
        name = input("Enter name: ")
        # find position of name
        n = mm.find(name.encode())
        # go to end of name
        n1 = n + len(name)
        # dislays the next 10 bytes
        ph = mm[n1 : n1 + 10]
        print('Phone No: ',ph.decode())

    # modify phone no
    if ch == '3':
        name = input("Enter name: ")
        # find position of name
        n = mm.find(name.encode())
        # go to end of name
        n1 = n + len(name)
        # enter new phone number
        ph1 = input("Enter new phone number: ")
        mm[n1:(n1+10)] = ph1.encode()

    mm.close()


