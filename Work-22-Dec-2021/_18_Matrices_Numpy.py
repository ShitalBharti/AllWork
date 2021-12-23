"""
-> Matrix represents a rectangular array of elements arranged in row and columns.
-> single row = row matrix
-> single column = column matrix
-> To work with matrices, numpy provides special object called matrix.
"""
from numpy import *
# matrix creation
matrix_name = matrix([[1,2,3],[4,5,6]])
print(matrix_name)

print("--------------------------------------------")
# passing an 2D array
arr = [[1,2,3],[4,5,6]]
matrix1 = matrix(arr)
print(matrix1)

print("--------------------------------------------")
# passing a string
string1 = '1 2; 3 4; 5 6'
matrix2 = matrix(string1)
print(matrix2)

print("-----------------Getting diagonal elements---------------------------")
# Getting diagonal elements in a matrix
string2 = '1 2 3; 3 4 5; 6 7 8'  # create 3*3 matrix
matrix3 = matrix(string2)
d = diagonal(matrix3)  # inbuilt function
print(d)

print("-----------------Maximum & Minimum elements---------------------------")
max_no = matrix3.max()
print("Maximum no: ",max_no)
min_no = matrix3.min()
print("Minimum no: ",min_no)

print("-----------------Sum & Average  elements---------------------------")
sum_no = matrix3.sum()
print("Sum: ",sum_no)
avg_no = matrix3.mean()
print("Average: ",avg_no)

print("-----------------Product of elements---------------------------")
# to find product pass 0 for column wise product and 1 for row wise product
prodc = matrix3.prod(0)
print("Column wise: ",prodc)
prodr = matrix3.prod(1)
print("Row wise: ",prodr)

print("-----------------Sorting of elements---------------------------")
sort_m = sort(matrix3)
print("Sorted matrix: ",sort_m)

print("-----------------Transpose of Matrix---------------------------")
# rows will be column in transpose and column will be rows.
# size will remain same
# we can use transpose() and getT() method to find transpose.
matrix_o = matrix('1 2 3; 4 5 6; 7 8 9')
print("Original matrix: ",matrix_o)
matrix_t = matrix_o.transpose()
print("Transpose matrix: ",matrix_t)

