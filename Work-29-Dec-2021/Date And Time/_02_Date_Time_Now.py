"""
Current date and time in our computer system can be known using following:
    -> ctime() function of "time" module
    -> now() method of "datetime" class of "datetime" module
    -> today() method of "datetime" class of "datetime" module
"""
# to know current date and time using ctime() function

import time
from datetime import datetime
from datetime import date

t = time.ctime()
print(t)

# to know local date and time using now() method

now = datetime.now()
print(now)

# to know today's date and time using today() method
tdm = datetime.today()
print(tdm)

td = date.today()
print(td)
