"""
-> A decorator is a function that accepts a function as parameter and returns a function.
-> A decorator takes the result of a function, modifies the result and returns it.
-> It helps to perform some additional processing required by a function.

Steps to create decorators:
    -> Decorator function is define with another function name as parameter.
    -> Define a function inside decorator function.
    -> Return the inner function.

"""

# decorator program to increase the value of a function by 2

def decor(fun):             # this is decorator function
    def inner():            # this is inner function that modifies
        value = fun()
        return value + 2
    return inner            # return inner function

# function to which decorator should be applied
def num():
    return 10

# call decorator function and pass num
result_fun = decor(num)
print(result_fun())

print("-----------------------------")
# program to apply a decorator to a function using @ symbol

def decor(fun):             # this is decorator function
    def inner():            # this is inner function that modifies
        value = fun()
        return value + 2
    return inner            # return inner function

# function to which decorator should be applied
@decor
def num():
    return 10

print(num())







