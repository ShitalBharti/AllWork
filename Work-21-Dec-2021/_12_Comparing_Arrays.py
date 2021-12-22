from numpy import *
a = array([1,2,3,0])
b = array([0,2,3,1])

c = a == b
print("Result of a==b: ",c)
c = a > b
print("Result of a>b: ",c)
c = a < b
print("Result of a<b: ",c)

print("-----------------------------------------------")
# using any() and all() functions
print("If any one element is true: ",any(c))
print("If all elements are true: ",all(c))

if any(a > b):
    print("a contains atleast one element greater than those of b")

print("-----------------------------------------------")
# use of logical functions on arrays
a = array([1,2,3],int)
b = array([0,2,3],int)

c = logical_and(a>0, a<4)
print(c)
c = logical_or(b>=0, b==1)
print(c)
c = logical_not(b)
print(c)

print("-----------------------------------------------")
# to compare the corresponding elements of two arrays and retrieve the biggest elements
a1 = array([10,20,30,40,50], int)
b1 = array([1,21,3,40,51], int)

c = where(a1>b1, a1, b1)
print(c)

print("-----------------------------------------------")
# to retrieve non-zero elements from an array
a2 = array([1,2,0,-1,0,6],int)
c = nonzero(a2)
print(c)
print(a2[c])



