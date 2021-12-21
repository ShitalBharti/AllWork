# position finding using sequential search

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

# sequential search
flag = False

for i in range(len(x)):
    if s == x[i]:
        print("Found at position: ",i+1)
        flag = True
    if flag == False:
        print("Not found")