try:
    name = input("Enter file name: ")
    f = open(name, 'r')
except IOError:
    print("File not found: ",name)
else:
    n = len(f.readlines())
    print(name,'has',n,'lines')
    f.close()