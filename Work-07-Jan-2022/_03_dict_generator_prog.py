def new(dict):
    for x,y in dict.items():
        yield x,y
dict={1:'hi',2:'hello'}
b=new(dict)
print(b)
print(next(b))
print(next(b))
print(next(b))