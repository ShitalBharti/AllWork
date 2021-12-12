# remove an item from a tuple
"""
tuples are immutable so that we cannot add or remove element from tuple
1st way: convert tuple to list and use list.remove()
"""
tuple1 = (1,2,3,4,5,6)
print(tuple1)
list1 = list(tuple1)
list1.remove(2)
tuple1 = tuple(list1)
print("After Removing 2:",tuple1)