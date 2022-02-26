"""
Variables are containers for storing data values.
A variable is created the moment you first assign a value to it.
Variables do not need to be declared with any particular type, and can even change type after they have been set.
"""
age = 25
print(age)

"""
If you want to specify the data type of a variable, this can be done with casting.
You can get the data type of a variable with the type() function.
"""
id = int(25)
print(id)

"""
String variables can be declared either by using single or double quotes:
Variable names are case-sensitive.
"""
firstname = 'Shital'
last_name = "Bharti"
print(firstname)
print(last_name)

"""
Variable Names:-

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
Variable names with more than one word can be difficult to read.
"""
x = 10
carname = "BMW"
_glassType = 'Gorilla'
# 1Laptop="Dell"  # Gives an error
Laptop_1_Type = 'Dell'
Mobile = 8554833446
mobile = 85548
Mobile_1 = 85566
print('x:{}'.format(x))
print('carname:{}'.format(carname))
print('GlassType:{}'.format(_glassType))
print('Laptop Type:{}'.format(Laptop_1_Type))
print('Mobile no 1:{}'.format(Mobile))
print('Mobile no 2:{}'.format(mobile))
print('Mobile no 3:{}'.format(Mobile_1))

"""
Python allows you to assign values to multiple variables in one line.
And you can assign the same value to multiple variables in one line.
"""
a = b = c = 10, 20, 30
print(a)
print(b)
print(c)
a = b = c = 10
print(a)
print(b)
print(c)

# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

list1 = ['Apple',25,45.5,True]
fruit = list1[0]
price = list1[1]
weight = list1[2]
packed = list1[3]
print(fruit+' '+str(price)+' '+str(weight)+' '+str(packed))

"""
The Python print statement is often used to output variables.
To combine both text and a variable, Python uses the + character.
You can also use the + character to add a variable to another variable.
For numbers, the + character works as a mathematical operator.
"""

# If you try to combine a string and a number, Python will give you an error.

a = 10
name = 'Shital'
# ans = a+name  # Error
# print(ans)

"""
Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
Create a variable outside of a function, and use it inside the function.
"""
x = 'awesome'
def myFunc():
    print("Python is:{}".format(x))
myFunc()

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
Create a variable inside a function, with the same name as the global variable
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
"""

y = 'good'
def myFunc():
    y = 'very easy'
    print("Python is:{}".format(y))  # Value of Local variable will be print as o/p
myFunc()

"""
To create a global variable inside a function, you can use the global keyword.
If you use the global keyword, the variable belongs to the global scope.
"""
def myFunc():
    global y
    y = 'fantastic'

myFunc()
print("Python is:{}".format(y))  # Value of global variable will be print as o/p


"""
Also, use the global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, refer to the variable by using the global keyword.
"""
y = 'very easy'

def myFunc():
    global y
    y = 'interpreted'

myFunc()
print("Python is:{}".format(y))