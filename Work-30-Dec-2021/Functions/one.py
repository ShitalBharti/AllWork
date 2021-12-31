"""
Special variable __name__:
-> When a program is executed in Python, there is a special variable internally created by the name '__name__'.
-> This variable stores the information whether the program is executed as individual program or module.
-> If individual program : '__main__' is stored in name.
-> If module program: '__modulename__' is stored in name.

"""

def display():
    print('Hello python!')

if __name__ == '__main__':
    display()
    print("Program running..")
else:
    print("Module running...")


