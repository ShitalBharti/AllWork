"""
-> Generators are functions that return a sequence of values.
-> A generator function is written like an ordinary function but it uses 'yield' statement.
-> This statement is useful to return the value.
-> The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off.
-> When resumed, the function continues execution immediately after the last yield run.
-> This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
"""

# program to create a generator that returns a sequence of numbers from x to y
def mygen(x,y):
    while x<=y:
        yield x
        x += 1
g = mygen(5,10)

for i in g:
    print(i, end = ' ')

print("----------------------------")

# a generator that returns characters from A to C

def mygen1():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen1()

print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # error
