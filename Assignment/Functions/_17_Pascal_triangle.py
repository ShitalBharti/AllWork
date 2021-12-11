# print given Pascal's triangle
"""
Pascal’s triangle is a pattern of the triangle which is based on nCr, below is the pictorial representation of Pascal’s triangle.
"""
from math import factorial

# input n
n = 5
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    # for new line
    print()


