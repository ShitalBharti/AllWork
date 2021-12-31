import arith

arith.add(10,22)
result = arith.sub(10,5)
print("Result of subtraction = ",result)

"""
-----> using module belonging to different package

import mypack.arith
mypack.arith.add(10,22)
result = mypack.arith.sub(10,22)
print("Result of subtraction = ",result)
"""