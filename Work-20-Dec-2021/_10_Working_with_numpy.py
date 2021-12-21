"""
import numpy
arr = numpy.array([10,20,30,40,50])
print(arr)
"""
"""
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)
"""
from numpy import *
arr = array([10,20,30,40,50])
print(arr)


"""
Creating arrays using numpy:
1. Using array() function
2. Using linspace() function
3. Using logspace() function
4. Using arrange() function
5. Using zeros() and ones() functions
"""

# 1. Using array() function
print("--------------------------------------")
arr1 = array(['a','b','c','d'])
print(arr1)

print("--------------------------------------")
arr1 = array(['Shital','Vitthal','Shubham','Ajinkya'])
print(arr1)

print("--------------------------------------")
a = array([1,2,3,4,5])
arr1 = array(a)
print(arr1)

# 2. Using linspace() function
print("--------------------------------------")
arr1 = linspace(0,10,5)  # divide 0 to 10 into 5 parts and take those points in array
print(arr1," ")

# 3. Using logspace() function
print("--------------------------------------")
arr1 = logspace(1,4,5)  # divide 10 power 1 to 10 power to 4 into 5 equal parts and take those points in array
n = len(arr1)
for i in range(n):
    print("{:.2f}".format(arr1[i]),end = ' ')
print()

# 4. Using arrange() function
print("--------------------------------------")
arr1 = arange(2,11,2)  # creating an array with even numbers upto 10
print(arr1)

# 5. Using zeros() and ones() functions
print("--------------------------------------")
a = zeros(5, int)
print(a)
b = ones(5)  # default datatype is float
print(b)
