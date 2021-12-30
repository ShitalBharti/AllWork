"""
Importance of date and time:
    -> Employee's experience is counted depends upon joining date and time.
    -> Age is calculated based on birthday.
Python modules:
    -> datetime
    -> time
    -> calendar
datetime class:
    -> it contains attributes like: year, month, day, hour, minute, second, microsecond, tzinfo
date class:
    -> it contains attributes like: year, month, day
time class:
    -> it contains attributes like: hour, minute, second, microsecond, tzinfo
timedelta class:
    -> it is useful to handle the durations, duration may be difference between two date, time or datetime instances.
epoch:
    -> it is the point where time starts.
    -> default value is: 0.0 hours of January 1st current year.
"""

import time

epoch = time.time()
print(epoch)   # how many seconds has passed from 1st Jan 2021
dt = time.localtime(1640804101.8310308)   # localtime() will convert the seconds into date and time
print(dt)

# to get date, month , year
d = dt.tm_mday
m = dt.tm_mon
y = dt.tm_year
print("Current day: {}, Current month: {}, Current year: {}".format(d,m,y))

# to get hour, minute, seconds
h = dt.tm_hour
m = dt.tm_min
s = dt.tm_sec
print("Current hour: {}, Current minute: {}, Current seconds: {}".format(h,m,s))

# to convet epoch time into corresponding date and time
ct = time.ctime(1640804765.6317644)
print(ct)