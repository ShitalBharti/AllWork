#infinite iterators
class Infinite:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        num=self.num
        self.num+=5
        return num
obj=Infinite()
myiter=iter(obj)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Its going to infinte...if we want to stop that
#stopiterate method
#anything that can be loop over in python ---iterable
#To check the list has iter...
'''num=[1,2,3,4]
print(dir(num))
'''