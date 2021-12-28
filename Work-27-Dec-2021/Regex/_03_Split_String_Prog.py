# to split string into pieces where one or more non alpha numeric characters are found.

import re
string = 'This; is the: "Core" Python\'s book'
result = re.split(r'\w+',string)
print(result)

result1 = re.split(r'\W+',string)
print(result1)

"""
Conclusion: split() method returns the pieces as elements of a list.
            W+ :    It will return all the characters which are not alpha numeric, + will match 1 or more occurrences indicated by W.
"""

