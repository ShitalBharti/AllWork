"""
\ = Escape special character nature
. = Matches any character except new line
^ = Matches beginning of a string
$ = Matches ending of a string
[...] = Denotes a set of possible characters ex. [6b-d] matches any characters '6','b','c', or 'd'
[^...] = Matches every character except the one inside brackets.
(...) = Matches the regular expression inside the parenthesis and result can be captured.
R | S = Matches either regex R or regex S
"""

# search whether a given string starting with 'He' or not.
import re
string = 'Hello World'
res = re.search(r"^He",string)
if res:
    print("string start with He")
else:
    print("string not start with He")

# search a word at the ending of a string
res1 = re.search(r"World$",string)
if res1:
    print("string ends with World")
else:
    print("string not ends with World")

# search at the ending of a string by ignoring case
res2 = re.search(r"world$",string,re.IGNORECASE)
if res1:
    print("string ends with world")
else:
    print("string not ends with world")

# to retreive marks and names from a given string
string1 = "Rahul got 75 marks,Vijay got 55 marks, whereas Subbu got 98 marks."
marks = re.findall('\d{2}',string1)
print(marks)
names = re.findall('[A-Z][a-z]*',string1)
print(names)

# to retreive timings either 'am' or 'pm'
string2 = "The meeting may be at 8am or 9am or 4pm or 5pm"
res3 = re.findall(r'\dam|\dpm',string2)
print(res3)
