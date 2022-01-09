#iterator another method
numbers=[1,2,3,4,5]
value=numbers.__iter__()
print(value)  #it gives the address
item1=value.__next__()
print(item1)
#if we want to get next item
item2=value.__next__()
print(item2)
item3=value.__next__()
print(item3)
item4=value.__next__()
print(item4)
item5=value.__next__()
print(item5)
'''item6=value.__next__()
print(item6)'''
#PEP 3114 renamed iterator.next() to iterator.__next__(). This was implemented in version 3.0

numbers=[1,2,3,4,5]
value=iter(numbers)
item1=next(value)
item2=next(value)
print(item1)
print(item2)

