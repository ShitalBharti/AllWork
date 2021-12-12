# slice a tuple
tuple1 = (1,2,3,4,5,6)
print(tuple1)
print("Tuple Slicing:",tuple1[:3])
print("Tuple Slicing:",tuple1[3:])

# find the index of an item of a tuple
print(tuple1.index(2))

# find the length of a tuple
print(len(tuple1))

# convert a tuple to a dictionary
tups = [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]
tuple_dict = {}
for item in tups:
    tuple_dict.update({item[0]:item[1]})
print(tuple_dict)