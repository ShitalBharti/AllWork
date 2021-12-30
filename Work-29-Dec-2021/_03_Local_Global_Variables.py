a = 1
def myfunction():
    a = 2
    print(a)  # local variable
myfunction()
print(a)        # global variable

# global keyword: When a programmer wants to use the global variable inside a function, he can use the keyword 'global' before the variable in beginning.

b = 1
def myfunc():
    global b
    print(b)
    b = 2
    print(b)
myfunc()
print(b)

# to get a copy of a global variable into a function and work with it

c = 1
def myfun():
    c = 2
    x = globals()['c']
    print('Global var c= ',x)
    print('Local var c= ',c)
myfun()
print('Global var c= ',c)