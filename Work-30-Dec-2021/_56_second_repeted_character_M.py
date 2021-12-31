'''find the second repeated word in a given string'''
#from collections import Counter
def second_repeated(str1):
    str2=str1.split(' ')
    max=0
    for key in str2:
        if str2.count(key)>max:
            max=str2.count(key)
            maxvalue=key
    print(maxvalue)



str1="my ame is raksh my name is "
second_repeated(str1)