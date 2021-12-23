import sys
from numpy import *

r1,c1 = [int(a) for a in input("First matrix rows and cols: ").split()]
r2,c2 = [int(a) for a in input("Second matrix rows and cols: ").split()]

if c1!=r2:
    print("Multiplication not possible!")
    sys.exit()
string1 = input("Enter first matrix elements: \n")

x = reshape(matrix(string1), (r1,c1))

string2 = input("Enter second matrix elements: \n")

y = reshape(matrix(string2), (r2,c2))

z = x * y
print("Product of matrix: ",z)

