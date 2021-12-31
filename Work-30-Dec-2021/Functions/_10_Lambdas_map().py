"""
-> It is similar to filter() function but it acts on each element of the sequence and perhaps changes the elements.
-> format of map() function is:
    map(function, sequence)

"""

# program to find squares of elements in a list

def squares(x):
    return x*x
lst = [1,2,3,4,5]
res = list(map(squares,lst))
print(res)

print("----------------------------")

# program to find squares of elements in a list using lambda function
lst1 = [6,7,8,9]
res1 = list(map(lambda x: x*x,lst1))
print(res1)

print("----------------------------")

# program to find products of elements of two different lists using lambda function

lst1 = [1,2,3,4,5]
lst2 = [10,20,30,40,50]
lst3 = list(map(lambda x,y: x * y,lst1,lst2))
print(lst3)