#for loop as an iterator
'''my_obj=[1,2,3,4,5,6]
for i in my_obj:
    print(i)'''


my_obj2=[1,8,6,4,3,9]
iter_obj=iter(my_obj2)

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
#using infinite loop
while True:
    try:
        element=next(iter_obj)
        print(element)
    except StopIteration:
        break
