from numpy import *

a = matrix('1 2 3; 4 5 6')
b = matrix('2 2 2; 1 -1 2')
print("Matrix 1: \n",a)
print("Matrix 2: \n",b)
c = a + b
print("Addition of Matrices: \n",c)

print("---------------------------------------------")
c = a / b
print("Division of Matrices: \n",c)