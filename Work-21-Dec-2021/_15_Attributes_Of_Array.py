"""
Single Dimension array - If array contains only one row and multiple columns of one column multiple rows than the array is called as single or 1D array.
Multi Dimension array - If an array contains more than 1 row and 1 column.
"""
import numpy
from numpy import array

"""
---------------------------------------Attributes of an Array-----------------------------------
Numpy's array class is called ndarray.
Python's array class is different from numpy's array class.

**ndim Attribute - no of dimensions in an array
"""
print("---------Dimension of array------------------")
arr = array([1,2,3,4])
print("Original array: ",arr)
print(arr.ndim)

"""
**shape Attribute - shape of an array. e.g tuple
"""

print("---------Shape of array------------------")
arr = array([1,2,3,4])
print("Original array: ",arr)
print(arr.shape)
arr1 = array([[1,2,3],[4,5,6]])   # row length must be same or no. of columns must be same
print("Original array: ",arr1)
print(arr1.shape)

"""
**size Attribute - it gives total number of elements in array.
"""
print("---------Size of array------------------")
arr = array([1,2,3,4])
print("Original array: ",arr)
print(arr.size)
arr1 = array([[1,2,3],[4,5,6]])   # row length must be same or no. of columns must be same
print("Original array: ",arr1)
print(arr1.size)

"""
**itemsize Attribute - It gives memory size of array element in bytes.
"""
print("---------Itemsize of array------------------")
arr = array([1,2,3,4])
print("Original array: ",arr)
print(arr.itemsize)

"""
**dtype Attribute - It gives us datatype of elements in array.
"""
print("---------Datatype of array------------------")
arr = array([1,2,3,4])
print("Original array: ",arr)
print(arr.dtype)

"""
**nbytes Attribute - It gives total number of bytes occupied by an array.
"""
print("---------Total bytes of array------------------")
arr = array([1,2,3,4])
print("Original array: ",arr)
print(arr.nbytes)

"""
reshape() method - It is use to change the shape of an array.
"""
print("--------------reshape() method------------")
arr1 = numpy.arange(12)
print("Original array: ",arr1)
arr1 = arr1.reshape(2,6)
print("After reshape: ",arr1)

"""
flatten() method - It is useful to return a copy of array collapsed into one dimension.
"""
arr2 = array([[1,2,3],[4,5,6]])   # row length must be same or no. of columns must be same
print("Original array: ",arr2)
arr2 = arr2.flatten()
print("After Flatten: ",arr2)


