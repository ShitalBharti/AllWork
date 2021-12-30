"""
"timedelta" class of "datetime" module is useful to find the durations like difference between two dates or finding the date after adding a period to an existing date.
It is possible to know the future dates or previous dates using 'timedelta'
'timedelta' class object is available in format:
    -> timedelta(days = 0, seconds = 0, microseconds = 0, milliseconds = 0, minutes = 0, hours = 0, weeks = 0)
"""

# program to find future date and time from an existing date and time
from datetime import *
import random, time

d1 = datetime(2016, 4, 29, 16, 45, 0)

period1 = timedelta(days= 10, seconds = 10, minutes=20, hours=12)
print("The new date and time is: ",d1+period1)

# program to display the next 10 dates continuously
d = date.today()
print(d)

# d = date(1966,6,29)

for x in range(1,10):
    nextdate = d + timedelta(days = x)
    print(nextdate)

# program to accept date of births of two persons and determining the older person
d1,m1,y1 = [int(x) for x in input("Enter first person's birth date: ").split('/')]
b1 = date(y1,m1,d1)

d2,m2,y2 = [int(x) for x in input("Enter second person's birth date: ").split('/')]
b2 = date(y2,m2,d2)

if b1==b2:
    print("same age")
elif b1>b2:
    print("Second person is older")
else:
    print("First person is older")

# sort a group of given dates in ascending order
group = []

group.append(date.today())

d = date(2015, 6, 29)
group.append(d)
d = date(2014, 6, 30)
group.append(d)

group.append(d+timedelta(days = 25))

group.sort()
for d in group:
    print(d)


# program to generate random numbers in a range with some time delay between each number

for i in range(10):
    num = random.randrange(100,200,5)
    print(num)
    # suspend execution for 3.5 seconds
    time.sleep(3.5)
