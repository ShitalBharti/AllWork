#392. Is Subsequence


str1='abc'
str2='axbycz'
flag1=False
flag2=False
s1=len(str1)
s2=len(str2)

if s1>s2:
    for i in str2:
        if i in str1:
            flag1=True

if s2>s1:
    for i in str1:
        if i in str2:
            flag2=True
if flag1:
    print(str2,"is subsequence of",str1)
if flag2:
    print(str1,"is subsequence of",str2)
