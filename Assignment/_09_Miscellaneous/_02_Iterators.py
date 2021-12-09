# Iterator is an object in python consits of __iter__() and __next()__ methods
# __iter__() -> It will have argument as iterable such as string,list,tuple,dict
# __next__() -> It will have argument as __iter__() method return variable, it will return next element in sequence

# Example String

string = 'Hello, I am Python'
myit = iter(string)

print(next(myit))
print(next(myit))
print(next(myit))
