# Reading file using read() method
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string = f.read()             # -----> It will read total content of file according to saved
print(string)
f.close()

print("--------------------------------------------")
# Reading file using readlines() method ----> It will read all lines
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string = f.readlines()
print(string)
f.close()

print("--------------------------------------------")
# Reading file using readline() method  ---> It will read single line at a time
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string = f.readline()
print(string)
f.close()

print("--------------------------------------------")
# Reading file using read() method and splitlines() method  ---> It will read line by line by splitting lines
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string = f.read().splitlines()
print(string)
f.close()




