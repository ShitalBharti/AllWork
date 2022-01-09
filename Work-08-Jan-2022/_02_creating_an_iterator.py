#To create an iterator, we need to implement the methods
#iter() and next().
class Example:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=2
        return x
iterator=Example()
my_iter=iter(iterator)
print(next(my_iter))
print(next(my_iter))


