# python program to create a regular expressin to search for strings starting with m and having total 3 characters using the search() method.

import re

string = 'man sun mop run'
print("Original String: ",string)

print("-----------------search() method-----------------------")
result = re.search(r'm\w\w',string)  # search() method will extract only first string.
if result:                           # if result is not none.
    print(result.group())            # group() use to extract the string return by search() method.


# findall() method

print("-----------------findall() method-----------------------")
string = 'man sun mop run'
result = re.findall(r'm\w\w',string)  # findall() method will extract all strings.
if result:                           # if result is not none.
    print(result)                    # result is a list

# match() method

print("-----------------match() method-----------------------")
string = 'man sun mop run'
result = re.match(r'm\W\W',string)  # match() method will extract only first string.
if result:                           # if result is not none.
    print(result)                   # no o/p because W means not alphabet not numeric



"""
Conclusion: small w: represents any one alpha numeric characters. i.e A-Z, a-z, 0-9 
            capital W: represents any character that is not alpha numeric.
"""