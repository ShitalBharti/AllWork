"""
It is useful to ensure that a given condition is True. If it is not true, it raises AssertionError.
"""

# program using assert statement and catching AssertionError
try:
    x = int(input("Enter a number between 5 and 10: "))
    assert x>=5 and x<=10
    print('The number entered: ',x)
except AssertionError:
    print("The condition is not fulfilled")


# program to use the assert statement with a message

try:
    x = int(input("Enter a number between 5 and 10: "))
    assert x >= 5 and x <= 10, "Your input is not correct"  # this message is passed to obj
    print('The number entered: ', x)
except AssertionError as obj:
    print(obj)