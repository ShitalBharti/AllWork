# program to retrieve all words starting with 'a' in given string

import re
string = 'has an apple a day keeps a doctor away'
result = re.findall(r'a[\w]*',string)
print(result)

# program to create a regular expression to retrieve all words starting with a numeric digit.
string1 = "The meeting will be conducted on 1st and 21st of every month"
result1 = re.findall(r'\d[\W]*',string1)
for word in result1:
    print(word)

# program to create a regular expression to retrieve all words having 5 characters length.
string2 = "one two three four five six seven 8 9 10"
result2 = re.findall(r'\b\w{5}\b',string2)
print(result2)

# program to create a regular expression to retrieve all words having 5 characters length using search()
string3 = "one two three four five six seven 8 9 10"
result3 = re.search(r'\b\w{5}\b',string3)
print(result3.group())

# program to create a regular expression to retrieve all words having length of atleast 4 characters.
string4 = "one two three four five six seven 8 9 10"
result4 = re.findall(r'\b\w{4,}\b',string4)
print(result4)

# program to create a regular expression to retrieve all words having length 3 or 4 or 5 characters.
string5 = "one two three four five six seven 8 9 10"
result5 = re.findall(r'\b\w{3,5}\b',string5)
print(result5)

# program to create a regular expression to retrieve only single digit from a string
string6 = "one two three four five six seven 8 9 10"
result6 = re.findall(r'\b\d\b',string6)
print(result6)

# program to create a regular expression to retrieve last word of a string, if it starts with t.
string7 = "one two three one two three"
result7 = re.findall(r't[\w]*\Z',string7)
print(result7)