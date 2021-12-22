"""
Multidimensional arrays can be created in following ways:
1. Using array() function
2. Using ones() and zeroes() function
3. Using eye() function
4. Using reshape() function
"""
from numpy import *

print("------------------using array() function-------------------")
a = array([[1,2,3,4],[5,6,7,8]])
print(a)

print("------------------using ones() function-------------------")
a = ones((3,4),int)
print(a)

print("------------------using zeroes() function-------------------")
a = zeros((3,4),int)
print(a)

print("------------------using eye() function-------------------")
a = eye(3)
print(a)

print("------------------using reshape() function-------------------")
a = array([1,2,3,4,5,6])
print("Original array: ",a)
b = reshape(a,(2,3))
print(b)
