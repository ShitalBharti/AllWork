"""
-> It is useful to create calendar for any month or year.
-> It is also useful to know whether a given year is leap year or not.
-> The isleap() function of calendar module is useful for this purpose.
"""

# program to enter a year number and display whether it is leap or not

from calendar import *

y = int(input("Enter year: "))
if(isleap(y)):
    print("Leap year")
else:
    print("Not leap year")

# program to display the calendar for a given month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

string = month(yy,mm)
print(string)

# program to display the calendar for all months of given year
year = int(input("Enter year: "))
# calendar(year, w ,l,c,m) -> year::year, w::width between two columns, l::blank lines between two rows
# c::column-wise space between two months, m::no. of months to be displayed in one row
print(calendar(year, 2,1,8,3))