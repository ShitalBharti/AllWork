# create the colon of a tuple
from copy import deepcopy

tup_col = ('Hello',1,True,[])
print(tup_col)
print(type(tup_col)) # -> tuple
tup_col_crt = deepcopy(tup_col)
print(type(tup_col_crt))  # -> tuple
tup_col_crt[3].append(10)
print(tup_col_crt)
"""
The original elements before deep copying
1 2 [3, 5] 4
The new list of elements after deep copying
1 2 [7, 5] 4
The original elements after deep copying
1 2 [3, 5] 4
The original elements before shallow copying
1 2 [3, 5] 4
The original elements after shallow copying
1 2 [7, 5] 4 
"""
