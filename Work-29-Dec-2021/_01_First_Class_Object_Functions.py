"""
->  In python, functions are considered as first class objects.
->  It means, we can use functions as perfect objects.
->  In fact when we create a function, Python Interpreter internally, creates an object.
->  Since functions are objects, we can pass a function to another function just like we pass an object(or value) to function.
->  Also, it is possible to return a function from another function.
->  This is similar to returning an object (or value) from a function.

Points:
->  It is possible to assign a function to a variable.
->  It is possible to define one function inside another function.
->  It is possible to pass a function as parameter to another function.
->  It is possible that a function can return another function.
"""

# assign function to a variable
def display(string):
    return 'Hai'+string
x = display('Krishna')
print(x)

# define function inside another function

def display(string):
    def message():
        return 'How are you?'

    result = message() + string
    return result
print(display('Krishna'))

# program to know how to pass a function as parameter to another function

def display(fun):
    return 'Hai '+fun

def message():
    return 'How are U?'

print(display(message()))

# program to know how a function can return another function

def display():
    def message():
        return 'How are you?'

    return message

fun = display()
print(fun)
print(fun())





