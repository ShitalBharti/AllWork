# A function that calls itself is known as 'recursive function'.

# program to calculate factorial values using recursion
def factorial(n):
    if n==1:
        res = 1
    else:
        res = n * factorial(n-1)
    return res

for i in range(1,11):
    print('Factorial of {} is {}'.format(i, factorial(i)))