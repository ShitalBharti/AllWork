# program to create datetime object by combining date and time objects.

from datetime import datetime
from datetime import date
from datetime import time

d = date(2021,12,29)
t = time(11,20)
dt = datetime.combine(d,t)
print(dt)

# program to create datetime object and then change its contents.

dt1 = datetime(year = 2022, month = 11, day = 25, hour = 15, minute = 30, second = 22)
print(dt1)

dt2 = dt1.replace(year = 2023, hour = 20, month = 12)
print(dt2)

