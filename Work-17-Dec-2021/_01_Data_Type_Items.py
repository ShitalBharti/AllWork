# Prints each item and its corresponding type from the following list
dict1 = {'name':'shital', 'id':101, 'salary':74500.45, 'Gender':'Female','Married':True}
for key,value in dict1.items():
    print("Type {}:: key {}".format(type(key),key))
    print("Type {}:: value {}".format(type(value),value))
    print("---------------------------------------")

#To sort (ascending and descending) a dictionary by value
dict2 = {'shital_id':1, 'rakshitha_id':3, 'srilekha_id':2}
oplist = sorted(dict2.items(),key = lambda value: value[1])
print("Sorted dictionary by value: ",oplist)

#Add a key to a dictionary
print("---------------------------------------")
dict3 = {'s1':1,'s2':2}
dict3['s3'] = 3
print(dict3)

# Check if a given key already exists in a dictionary.
print("---------------------------------------")
print("Given dictionary is: ",dict1)
key_el = input("Enter key: ")
if key_el in dict1:
    print("Key present")
else:
    print("Not present")

# Merge two Python dictionaries
print("---------------------------------------")
dict_1 = {1:'a', 2:'b'}
dict_2 = {3:'c',4:'d',2:'e'}
dict_1.update(dict_2)
print("Merge two dictionaries: ",dict_1)

# Sum all the items in a dictionary
print("---------------------------------------")
_1dict = {'subj1':100, 'subj2':50, 'subj3':70}
print("Given dict is: ",_1dict)
print("Sum of values: ",sum(_1dict.values()))

# Multiply all the items in a dictionary
print("---------------------------------------")
_1dict = {'subj1':100, 'subj2':50, 'subj3':70}
print("Given dict is: ",_1dict)
mul = 1
for i in _1dict.values():
    mul = mul * i
print("Multiplication of values: ",mul)

# Get the maximum and minimum value in a dictionary
print("---------------------------------------")
_1dict = {'subj1':100, 'subj2':50, 'subj3':70}
print("Given dict is: ",_1dict)
print("Maximum value: ",max(_1dict.values()))
print("Minimum value: ",min(_1dict.values()))

# Remove duplicates from Dictionary
print("---------------------------------------")
"""
The original dictionary is : {‘gfg’: 10, ‘for’: 10, ‘geeks’: 20, ‘is’: 15, ‘best’: 20}
The dictionary after values removal : {‘gfg’: 10, ‘geeks’: 20, ‘is’: 15}
"""
dict_original = {'gfg': 10, 'for': 10, 'geeks': 20, 'is': 15, 'best': 20}
opdict = {}
temp = []
for i, j in dict_original.items():
    if j not in temp:
        temp.append(j)
        opdict[i] = j
print(opdict)

# Combine two dictionary adding values for common keys
print("---------------------------------------")
dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
dict2 = {1:'f',2:'g',6:'h'}
dict3 = {}
print("first dictionary: ",dict1)
print("second dictionary: ",dict2)
element = [el for el in dict1.keys()]
for item in element:
    if item in dict2.keys():
        dict3[item] = dict1.get(item) + dict2.get(item)
    else:
        dict3[item] = dict1.get(item)
for key in dict2.keys():
    if key not in dict1.keys():
        dict3[key] = dict2.get(key)
print("after adding values: ",dict3)














