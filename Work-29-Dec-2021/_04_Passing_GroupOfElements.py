# function accept a group of numbers and find their total average

def calculate(lst):
    n = len(lst)
    sum1 = sum(lst)
    avg = sum1/n
    return sum1,n

print('Enter numbers separated by space: ')
lst = [int(x) for x in input().split()]

x,y = calculate(lst)
print('Total: ',x)
print('Average: ',y)
