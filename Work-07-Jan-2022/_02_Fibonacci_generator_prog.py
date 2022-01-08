'''Fibonacci series:
A series of numbers where in each number also called as the
Fibonacci number is the sum of the two preceding numbers.'''
def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x>20:
        break
    print(x,end=' ')




