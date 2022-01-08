#Generator Expressions can be used with for loop to produce iterators.
#generator expressions create anonymous generator functions
#resemble list comprehensions

f=range(4)
'''print('List comprehension')
g=[x+2 for x in f]
print(g)'''
print('generator expression')
r=(x+2 for x in f)
print(r)#returns generator object
#To print the values using generator expression
for x in r:
    print('using generator expression:',x)

#to print the minimum value in of the generator
print('minimum',min(r))