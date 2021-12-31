"""
-> A lambda function is a small anonymous function.(A function without name is called 'Anonymous function")
-> This are not defined using 'def'
-> This are defined using keyword 'lambda'
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
    x = lambda a : a + 5 # here 'a' is parameter name
    z = x(5)            # passing 5 as an argument using reference variable name, z is storing the o/p of function
    y = int(input("Enter number:"))
    res = y + z
    print("Result",res)
    print("--------------------------------------")

add()


fun = lambda x: x*x
value = fun(5)
print("Square is: ",value)

print("--------------------------------------")
# with multiple arguments
func = lambda x,y : x + y
result = func(5,4)
print("Addition is: ",result)

print("--------------------------------------")
# to find bigger number in two given number
maxno = lambda x,y : '{} is greater'.format(x) if x > y else '{} is greater'.format(y)
n1,n2 = [int(x) for x in (input("Enter two numbers: ").split(','))]
result = maxno(n1,n2)
print(result)
