#389. Find the Difference

str1='abcd'
str2='abc'

s1=len(str1)
s2=len(str2)

if s1>s2:
    print("character has been removed",str1[s2:])
else:
    print("character has been added",str2[s1:])