# Create an array of 5 integers and display the array items. Access individual element through indexes.
from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])

# Append a new item to the end of the array.

print("------------Append--------------")
print("Original array: "+str(array_num))
print("Append 11 at the end of the array:")
array_num.append(11)
print("New array: "+str(array_num))

print()

# Reverse the order of the items in the array.
print("------------Reverse--------------")
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))

print()

# Get the length in bytes of one array item in the internal representation.
print("------------Lenght in bytes--------------")
print("Length in bytes of one array item: "+str(array_num.itemsize))

print()

# Get the current memory address and the length in elements of the buffer used to hold an arrays? contents and also find the size
print("------------ Memory address--------------")
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))

print()

# Get the number of occurrences of a specified element in an array
print("------------ No. of occurrences--------------")
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))

print()

# Append items from inerrable to the end of the array
print("------------ Inerrable/ extend array--------------")
array_num.extend(array_num)
print("Extended array: "+str(array_num))

print()

# Convert an array to an array of machine values and return the bytes representation
print("------------ converting an array bytes to strings--------------")
print("Bytes to String: ")
x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)

# Append items from a specified list.
print()
print("------------ Appends item from list--------------")
num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Items in the array: "+str(array_num))

# Insert a new item before the second element in an existing array.
print()
print("------------ Insert new item--------------")
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.insert(1, 4)
print("New array: "+str(array_num))

# Remove a specified item using the index from an array.
print()
print("------------ Remove specific item--------------")
array_num.pop(2)
print("New array: "+str(array_num))

# Remove the first occurrence of a specified element from an array.
print()
print("------------ Remove first occurrence of specific item--------------")
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
array_num.remove(3)
print("New array: "+str(array_num))

# Convert an array to an ordinary list with the same items.
print()
print("------------ Convert an array to list--------------")
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)

