# print a tuple with string formatting
tuple1 = (1,2,3,4,5,6,7)
print("This is a tuple {}".format(tuple1))
print("This is a %s tuple" % (tuple1,))

print("-------------------------------------------")

#  replace last value of tuples in a list
tuple_sample = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print("Original tuple list:",tuple_sample)
opsample = []
for item in tuple_sample:
    tuple1 = item[:-1] + (100,)
    opsample.append(tuple1)
print("append 100 to last element:",opsample)

print("-------------------------------------------")

#  to remove an empty tuple(s) from a list of tuples
tuple_list = [(1,2,3),(4,5),(),(5,6),()]
print("Original tuple list:",tuple_list)
for item in tuple_list:
    if item == ():
        tuple_list.remove(())
print("Removing empty tuple:",tuple_list)

print("-------------------------------------------")
# sort a tuple by its float element.
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
    ('anand', '4.256'), ('gaurav', '10.365')]
print(sorted(tup, key = lambda x : float(x[1])))

print("-------------------------------------------")

#  count the elements in a list until an element is a tuple
list1 = [10,20,30,10,(20,),40]
print("Original List:",list1)
count = 0
for item in list1:
    if type(item) == tuple:
        break
    else:
        count += 1
print("Total Elements:",count)