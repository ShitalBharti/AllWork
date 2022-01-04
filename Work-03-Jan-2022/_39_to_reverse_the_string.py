'program to retuen the reverse ofthe string'
def reverse(str1):
    str=' '
    for i in str1:
        str=i+str
    return str
str1="mynameisrakshitha"
print(reverse(str1))