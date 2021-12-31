'''Find the first  non-repeated character in a string'''
from collections import Counter
def nonrepeating(string):
    freq=Counter(string)
    for i in string:
        if(freq[i]==1):
            print(i)
            break


string="india is a beutiful country"
nonrepeating(string)
