"""
-> Array can store only one type of data.
-> Array can increase or decrease their size dynamically. We need not declare size of an array.
-> Arrays are similar to lists. When dealing with huge number of elements, arrays use less memory than lists and offer faster execution than lists.

Type codes to create Arrays:
b - signed integer - 1
B - unsigned integer - 1
i - signed integer - 2
I - unsigned integer - 2
l - signed integer - 4
L - unsigned integer - 4
f - floating point - 4
d - double precision floating point - 8
u - unicode character - 2
"""

import array
a = array.array('i',[5,6,-7,8])
print("Array Elements:")
for i in a:
    print(i)
