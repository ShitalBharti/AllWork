"""
With statement - it can be used while opening a file
                - Advantage of with statement is that it will take care of closing a file which is opened by it.
                - Hence, we need not close this file explicitly
                - In case of exception also, with statement will close the file before exception is handled.
        syntax  - with open('filename','openmode') as fileobject:
"""
# to open file to read
with open('C:\\Users\\Admin\\Desktop\\hello.txt','r') as f:
    string = f.read()
    print(string)

# to write data in file
with open('C:\\Users\\Admin\\Desktop\\withstatement.txt','w') as f:
    string = "I hope you are doing well!"
    f.write(string)

# to write and append data in file
with open('C:\\Users\\Admin\\Desktop\\withstatementappend.txt','a') as f:
    string = "I hope you are doing well! & Have a great day ahead!"
    f.write(string)

