"""
-> filter() function is used to filter out the elements of a sequence depending on the result of a function.
-> We need to supply a function and a sequence to the filter() function as:
    filter(function,sequence)
-> function represents function name that may return True or False.
-> sequence represents a list, string or tuple.
"""

# program to filter out even numbers from a list

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

lst = [10,23,45,46,70,99]

# ans_lst = filter(is_even,lst)  # it will store the reference of filter object
ans_lst = list(filter(is_even,lst))  # it will store the elements into another list
print(ans_lst)

print("------------------------------------------")

# program to filter out even numbers from a list using lambda function
lst = [10,23,45,46,70,99]
res = list(filter(lambda x : x % 2 == 0,lst))
print(res)
