"""
-> The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off.
-> When resumed, the function continues execution immediately after the last yield run.
-> This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
"""

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


#  Fibonacci Number - using yield keyword

def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

print("\nUsing for in loop")
for i in fib(5):
    print(i)