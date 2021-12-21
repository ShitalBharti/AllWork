from array import *

x = array('i',[])

print("How many elements? ")
n = int(input())

for i in range(n):
    print("Enter element: ")
    x.append(int(input()))

print('Original Array: ',x)

# bubble sort
flag = False

for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            flag = True
    if flag == False:
        break
    else:
        flag = False

# print sorted array
print("Sorted Array: ",x)