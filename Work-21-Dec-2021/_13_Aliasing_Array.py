"""
Aliasing - new name given to existing array, memory is not allocated to new name
View (shallow copy) - new array is created with an existing array, new memory location is allocated o new array (change is affected in both arrays)
Copy (Deep Copy)  - new array is created with an existing array, new memory location is allocated o new array (change is not affected in both arrays)
"""

from numpy import *

a = arange(1,6)  # create array a with elements 1 to 5
b = a            # give another name b to a
print("Original a: ",a)
print("Alias b:    ",b)

b[0] = 99
print("After Modification...")
print("Original a: ",a)
print("Alias b:    ",b)

print("---------------------Creating View-------------------------")
# to create a view of an existing array
a2 = arange(1,6)  # create array a with elements 1 to 5
b2 = a2.view()     # create a view of a and call it b
print("Original a: ",a2)
print("View b:    ",b2)

b2[0] = 99
print("After Modification...")
print("Original a: ",a2)
print("View b:    ",b2)

print("---------------------Creating Copy-------------------------")
a1 = arange(1,6)
b1 = a1.copy()  # create a copy of a and call it b
print("Original a: ",a1)
print("Copy b:    ",b1)

b1[0] = 99
print("After Modification...")
print("Original a: ",a1)
print("Copy b:    ",b1)
