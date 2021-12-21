from array import *

# taking marks from user
lst = [int(i) for i in input('Enter marks: ').split(',')]

# creating an array to store marks
marks = array('i', lst)

# display marks and find total
total = 0
for x in marks:
    print(x)
    total += x
print("Total marks: ",total)

# display percentage
n = len(marks)
percent = total/n
print("Percentage: {:.2f}".format(percent))