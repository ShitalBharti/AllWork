"""
-> A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
-> If the body of a def contains yield, the function automatically becomes a generator function.
"""


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)