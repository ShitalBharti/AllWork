'''find the first repeted character in the string'''
from collections import Counter
def first_repeating(string):
    freq=Counter(string)
    for i in string:
        if(freq[i]>1):
            print(i)
            break
string="today is rainning heavily"
first_repeating(string)
