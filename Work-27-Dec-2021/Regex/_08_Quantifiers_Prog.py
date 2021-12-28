"""
+ = 1 or more repetitions of the preceding regexp
* = 0 or more repetitions of the preceding regexp
? = 0 or 1 repetitions of the preceding regexp
{m} = exactly m occurrences
{m,n} = from m to n, m defaults to 0, n defaults to infinity
"""

# program to create a regular expression to retrieve the phone number of a person
import re
string = 'Nageswara Rao: 1234567891'
res = re.search(r'\d+',string)
print(res.group())

# program to create a regular expression to extract only name but not phone number from a string
string1 = 'Nageswara Rao: 1234567891'
res1 = re.search(r'\D+',string1)
print(res1.group())

# program to create a regular expression to find all words starting with 'an' or 'ak'.
string2 = "anil akhil anant arun arati arundhati abhijit ankur"
res2 = re.findall(r'a[nk][\w]*',string2)
print(res2)

# retrieve date of births from a string
string3 = "Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000"
res3 = re.findall(r'\d{2}-\d{2}-\d{4}',string3)
print(res3)

string3 = "Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000"
res3 = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',string3)
print(res3)
