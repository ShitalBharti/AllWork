from array import *

# character array
arr1 = array('u',['a','b','c','d','e'])
print("Character Array::")
for ch in arr1:
    print(ch)
    # print(type(ch)) -> str
print("---------------------------------------------------------")
# floating array
arr2 = array('d',[10.5,9.6,4.56,3.56,7.80])
print("Floating Array::")
for ch in arr2:
    print(ch)
print("---------------------------------------------------------")
# creating one array from another array
arr3 = array('d',[1.5, 3.4, 5.6, 7])
arr4 = array(arr3.typecode,(a*3 for a in arr3))
print("Second Array::")
for ch in arr4:
    print(ch)
print("---------------------------------------------------------")
# length of an array
length = len(arr4)
print(length)
print("---------------------------------------------------------")
# accessing elements of an array using for loop
for i in range(length):
    print(arr4[i],end=' ')
print()
print("---------------------------------------------------------")
# accessing elements of an array using while loop
i = 0
while i < length:
    print(arr4[i],end =' ')
    i += 1
print()
print("---------------------------------------------------------")

# array slicing -> arrayname[start:stop:stride] stride represents step size excluding starting element
for i in arr1[1:4]:
    print(i)
print("---------------------------------------------------------")



