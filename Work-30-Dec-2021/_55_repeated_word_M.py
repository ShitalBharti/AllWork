'''find the first repeated word in a given string'''
from collections import Counter
def first_repeting(str1):
    str2=str1.split(' ')
    freq=Counter(str2)
    for key in str2:
        if(freq[key]>1):
            print(key,str1.index(key))
            break


str1="my name is my name is shital"
first_repeting(str1)
