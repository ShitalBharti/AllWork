"""
-> A lambda function is a small anonymous function.
-> A lambda function can take any number of arguments, but can only have one expression.
-> The power of lambda is better shown when you use them as an anonymous function inside another function.
-> Use lambda functions when an anonymous function is required for a short period of time.
"""
x = lambda a : a + 5
print(x(5))
print("--------------------------------------")

x = lambda a : a * 5
print(x(6))
print("--------------------------------------")

def add():
    x = lambda a : a + 5
    z = x(5)
    y = int(input("Enter number:"))
    res = y + z
    print("Result",res)
    print("--------------------------------------")

add()



