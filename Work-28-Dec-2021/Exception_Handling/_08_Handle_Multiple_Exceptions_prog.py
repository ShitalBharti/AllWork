
def avg(list1):
    tot = 0
    for x in list1:
        tot += x
    avg = tot/len(list1)
    return tot,avg

try:
    t,a = avg([1,2,3,4,5,'a'])
    print("Total = {}, Average = {}".format(t,a))
except TypeError:
    print('Type error, please provide numbers..')
except ZeroDivisionError:
    print("Please do not give empty list...")
