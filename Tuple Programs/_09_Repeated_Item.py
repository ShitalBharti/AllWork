#  find the repeated items of a tuple

tuple_1 = (1,2,2,3,3,4,5,6,6,'Shital','Shital')
repeated_item = []
for item in tuple_1:
    if tuple_1.count(item) > 1:
        repeated_item.append(item)
print("Original tuple:",tuple_1)
print("Repeated items:",set(repeated_item))