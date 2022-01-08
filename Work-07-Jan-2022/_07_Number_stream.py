#number stream can be any numbers...even numbers,odd numbers
#number stream using generator expression.
a=range(100)
b=(x for x in a)
print(b) #returns generator object
for i in b:
    print('number stream',i)

#to print even  numbers
a=range(2,100,2)
b=(x for x in a)
print(b) #returns generator object
for i in b:
    print('even stream',i)

#to print odd numbers
a=range(1,100,2)
b=(x for x in a)
print(b) #returns generator object
for i in b:
    print('odd stream',i)
