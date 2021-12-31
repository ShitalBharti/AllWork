'''find the first repeated character of a given string where the index of the first occurence is small '''
from collections import Counter
def first_repeating(string):
    freq=Counter(string)
    for i in string:
        if(freq[i]>1):
            print(i,string.index(i))
            break
string="today is rainning heavily"
first_repeating(string)
