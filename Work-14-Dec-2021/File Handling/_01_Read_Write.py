# to write in the file   -----> Overwrite the previous contents
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','w')
string = input("Enter text:")
f.write(string)
f.close()

print("--------------------")

# to append the data in file  -----> Append the new contents at the end of the file
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','a')
string = input("Enter text:")
f.write(string)
f.close()

print("--------------------")
# to read content in the file   -----> To read the contents of the file
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string1 = f.read()
print(string1)
f.close()

print("--------------------")
# to read limited content in the fie
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string1 = f.read(22)       # -----> to read only 22 characters from file
print(string1)
f.close()

