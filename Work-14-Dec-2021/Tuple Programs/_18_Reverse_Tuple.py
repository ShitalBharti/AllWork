# reverse a tuple

# 1. Using list to reverse tuple
tuple_create = (1,2,3,4,5,6,7,8,9)
print("Original tuple:",tuple_create)
list1 = list(tuple_create)
list1.reverse()
op_tuple = tuple(list1)
print("Reverse tuple:",op_tuple)

print("--------------------------------------------------")

# 2. Using reversed() built in function
tuple2 = (11,12,13,14,15,16,17)
print("Original tuple:",tuple2)
optuple = ()
for item in reversed(tuple2):
    optuple = optuple + (item,)
print("Reverse tuple:",optuple)