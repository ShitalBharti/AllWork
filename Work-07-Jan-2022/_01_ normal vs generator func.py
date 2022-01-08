#difference between normal functions and generator functions
'''Generator functions              Normal Functions
Make use of 'yield' keyword         make use of 'return' keyword
Run when 'next()'method is called   Run when name of the method is called
produce items one at a time and     produce all the items at once.
only when required
'''

#writing generator function :
def func():
    a = [1,2,3]
    for el in a:
        yield el

b=func(a)
next(b)
'''for i in b:
    print(i)'''
print(next(b))