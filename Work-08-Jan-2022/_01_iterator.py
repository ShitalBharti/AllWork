#An iterator is an object that contains a sequence or
#countable values that can be traversed upon.
#Iterables are objects that act as iterable containers.
#tuples,lists,sets,range can be treated as iterables.

my_obj=['python','iterator','Machine Learning']
iter_obj=iter(my_obj)
#using the next function to iterate
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

#we can use tuple,set also....
'''
my_obj1={1,2,3}
iter_obj=iter(my_obj1)
print(next(iter_obj))

my_obj2='string'
iter_obj=iter(my_obj2)
print(next(iter_obj))

'''
'''Why it is used:
Iterators are very powerful tools when dealing with large amount of data
save resources as they return one element at a a time
we can deal with infinite data and infinite memory'''



