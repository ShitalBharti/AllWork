"""
Logical Operators: and, or, not
"""
import gc

x,y = 10,20
print('and:->',x<y and y<30)
print('or:->',x<y or y<x)
print('not:->',not(x>y))
_a = 10
print(_a)

a = 10
print(gc.disable())
a = 20
print(a)
