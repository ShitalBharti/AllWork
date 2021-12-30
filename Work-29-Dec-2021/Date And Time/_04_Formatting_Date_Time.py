"""
Contents of "datetime","date","time" classes objects can be formatted using "strftime()" method -> string format of time
"""

# program to convert a date into a required string format
from datetime import date

td = date.today()
print(td)

string = td.strftime("{},{},{}".format(td.year,td.month,td.day))
print(string)

string1 = td.strftime("%d, %B, %Y")
print(string1)

"""
Format codes used in strftime() method:

format code         Meaning                                             Example
%a                  Weekday as abbreviated name                         Sun,Mon,..Sat
%A                  Weekday as full name                                Sunday,..Saturday
%w                  Weekday as decimal number                           0,1...6
%d                  Day as zero added decimal number                    01,02,...31
%b                  Month as abbreviated name                           Jan,Feb,..Dec
%B                  Month as full name                                  January,..December
%m                  Month as zero added decimal number                  01,02,...,12
%-m                 Month as decimal number                             1,2,...,12
%y	                Year without century as zero added decimal no.      00, 01, …, 99
%-y	                Year without century as decimal number.	            0, 1, …, 99
%Y	                Year with century as decimal number.	            2013, 2019 etc.
%H	                Hour(24-hour clock) as zero added decimal no.	    00, 01, …, 23
%-H	                Hour (24-hour clock) as a decimal no.	            0, 1, …, 23
%I	                Hour (12-hour clock) as zero added decimal no.	    01, 02, …, 12
%-I	                Hour (12-hour clock) as a decimal no.	            1, 2, … 12
%p	                Locale’s AM or PM.	                                AM, PM
%M	                Minute as a zero added decimal no.	                00, 01, …, 59
%-M	                Minute as a decimal no.	                            0, 1, …, 59
%S	                Second as a zero added decimal no.	                00, 01, …, 59
%-S	                Second as a decimal no.	                            0, 1, …, 59
%f	                Microsecond as decimal no,zero added on the left.	000000 – 999999
%z	                UTC offset in the form +HHMM or -HHMM.	 
%Z	                Time zone name.	 
%j	                Day of the year as zero added decimal no.	        001, 002, …, 366
%-j	                Day of the year as a decimal no.	                1, 2, …, 366
%U	                Week number of the year 
                    (Sunday as the first day of the week). 
                    All days in a new year preceding the first 
                    Sunday are considered to be in week 0.	            00, 01, …, 53
%W	                Week number of the year 
                    (Monday as the first day of the week). 
                    All days in a new year preceding the first 
                    Monday are considered to be in week 0.	            00, 01, …, 53    
%c                  Appropriate date and time representation.           Tue Aug 16 21:30:00 1988
%x                  Appropriate date representation.                    08/16/88
%%                  A single % character.                               %
"""