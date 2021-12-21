from numpy import *

arr = array([10,20,30.5,-40])
print("Original array:      {}".format(arr))

# Arithmetic Operations
print("After Adding 5:      {}".format(arr + 5))
print("After Subtracting 5: {}".format(arr - 5))
print("After Multiplying 5: {}".format(arr * 5))
print("After dividing 5:    {}".format(arr / 5))
print("After modulus with 5:{}".format(arr % 5))

# Arrays in expression
print("Expression value:    {}".format((arr+5)**2 - 10))

# Math functions
print("sin values:           {}".format(sin(arr)))
print("cos values:           {}".format(cos(arr)))
print("tan values:           {}".format(tan(arr)))
print("biggest element:      {}".format(max(arr)))
print("smallest element:     {}".format(min(arr)))
print("sum of all elements:  {}".format(sum(arr)))
print("average of all elements: {}".format(mean(arr)))