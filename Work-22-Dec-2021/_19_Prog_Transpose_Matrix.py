# to accept matrix as input and print transpose of matrix

from numpy import *

r,c = [int(a) for a in input("Enter rows and cols: ").split()]

str = input("Enter matrix elements:\n")

x = reshape(matrix(str),(r,c))
print("Original matrix: ",x)

y = x.transpose()
print("Transpose matrix: ",y)