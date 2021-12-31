"""
-> It reduces the sequence of elements into a single value by processing the elements according to a function supplied.
-> Format of reduce() function is:
    reduce(function, sequence)
"""

# program to calculate products of elements of a list

from functools import reduce   # reduce() function belongs
lst = [1,2,3,4,5]
res = reduce(lambda x,y: x*y,lst)
print("product=",res)

# program to calculate sum of elements

sum_el = reduce(lambda x,y:x + y,lst)
print("addition=",sum_el)
