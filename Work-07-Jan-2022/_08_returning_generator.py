'''def myfunc(a):
    while a<=3:
        yield a
        a+=1

b=myfunc(2)# b is the generator object
print(next(b))
print(next(b))
print(next(b))
'''

def ex():
    n=3
    yield n #first returns this
    n=n*n
    yield n
d=ex()
print('ex:',next(d))
print(next(d))

#If we want to execute the generator function at once,can use
#for loop

#Generators with loops

def ex():
    n=3
    yield n #first returns this
    n=n*n
    yield n
d=ex()
for j in d:
    print('with loops',j)
