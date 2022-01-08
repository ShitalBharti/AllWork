'''Generators:
---Are functions that return traversable objects or items
---produce items one at a time and only when required.
---are run along with 'for' loops.
---whenever a false statement is included to iterator over a set
    of items a generator function is run.
---It is responsible to generate a sequence of values.
---can write generator like ordinary functions,but uses yield
    keyword to return values'''
'''
def mygen():
    yield 'a'
    yield 'b'
g=mygen()
print(g) #gives the address
print(next(g))
print(next(g))
print(next(g))


'''

def countdown(num):
    print('start countdown')
    while (num>0):
        yield num
        num+=1
values=countdown(10)

for x in values:
    print('countdown',x)

'''Advantages of Generators:
----without generators producing iterators is extremly difficult and lengthy
----generators make our task very simple because they do iter and next methods automatically
----Better memory management and utilization(items are required whenever we are required)
----can be used to produce infinite items
----'''

