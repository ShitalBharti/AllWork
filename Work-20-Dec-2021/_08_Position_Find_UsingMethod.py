from array import *

x = array('i',[])

print("How many elements? ")
n = int(input())

for i in range(n):
    print("Enter element: ")
    x.append(int(input()))

print('Original Array: ',x)

print("Enter element to search: ")
s = int(input())

try:
    pos = x.index(s)
    print("Found at position: ",pos + 1)

except ValueError:
    print("Not Found")
