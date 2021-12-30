# program to find day of the year and week day name.
from datetime import *

td = date.today()
print(td)

s1 = td.strftime("%j")
print("Today is",s1,"Day of the current year")

s2 = td.strftime("%A")
print("It is",s2)

# program to format the time using strftime() method

dt = datetime.now()
print(dt)

print("Current time: ",dt.strftime("%H:%M:%S"))

# program to accept a date from the keyboard and display the day of the week

d,m,y = [int(x) for x in input("Enter a date: ").split('/')]

dt = date(y,m,d)

print(dt.strftime('Day %w of the week. This is %A'))

# program to find difference in number of days, weeks and months between two given dates

d1,m1,y1 = [int(x) for x in input("Enter first date: ").split('/')]
d2,m2,y2 = [int(x) for x in input("Enter second date: ").split('/')]

dt1 = date(y1,m1,d1)
dt2 = date(y2,m2,d2)

dtdiff = dt1 - dt2
print("Days difference: ",dtdiff)

weeks,days = divmod(dtdiff.days,7)
print("Weeks difference: ",weeks)

months,days = divmod(dtdiff.days,30)
print("Months difference: ",months)

# program to find difference between two dates along with times

d1 = datetime(2000, 6, 25, 8, 00, 25)
d2 = datetime(2016, 5, 20, 7, 55, 15)

diff = d2-d1
print(diff)

weeks,days = divmod(diff.days, 7)
hrs,secs = divmod(diff.seconds, 3600)
mins = secs//60
secs = secs%60
print("Difference is %d weeks, %d days, %d hours, %d minutes and %d seconds" %(weeks,days,hrs,mins,secs))
