def firstn(num):
    n=1
    while n<=num:
        yield n
        n=n+1
values=firstn(10)
for x in values:
    print('first n numbers',x)