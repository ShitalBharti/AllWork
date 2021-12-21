from array import *

arr = array('i',[10,20,30,40,50])
print("Original array: ",arr)

print("-----------------------------------------------")
# append() method
arr.append(30)
arr.append(60)
print("After appending array: ",arr)

#inserting into 2 position insert() method
print("-----------------------------------------------")
arr.insert(2,99)
print("After inserting array: ",arr)

# remove() method
print("-----------------------------------------------")
arr.remove(40)
print("After removing 40: ",arr)

# pop() method
print("-----------------------------------------------")
n = arr.pop()
print("After pop: ",arr)
print("Popped element: ",n)

# index() method
print("-----------------------------------------------")
n = arr.index(30)
print("Index of element 30: ",n)

# tolist() method
print("-----------------------------------------------")
lst = arr.tolist()
print("Array: ",arr)
print("Convert to list: ",lst)
