# Slicing - It refers to extracting a range of elements from the array. Syntax: arrayname[start:stop:stepsize]

from numpy import *

a = arange(10,16)
print("Original array: ",a)

print("------------------Slicing-------------------------------")
b = a[1:6:2]
print(b)

print("-------------------------------------------------")
b = a[::]
print(b)

print("-------------------------------------------------")
b = a[-2:2:-1]
print(b)

print("-------------------------------------------------")
b = a[:-2:]
print(b)

# Indexing - It refers to locations of the elements. By specifying the location numbers from 0 onwards till n-1
print("----------------Indexing---------------------------------")
i = 0
length = len(a)
while i<length:
    print(a[i])
    i += 1