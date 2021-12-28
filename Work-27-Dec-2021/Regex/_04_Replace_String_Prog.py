# replace string wih a new string

import re
string = "Kumbhmela will conducted at Ahmedabad in India"
result = re.sub(r'Ahmedabad','Allahabad',string)
print(result)

string1 = 'I will call you at 5:00 PM'
result1 = re.sub(r'5:00','12:30',string1)
print(result1)

string2 = 'Dependancy injection helps us to make object\'s \'loosely\' coupled'
result2 = re.sub(r'\'loosely\'','\'loose\'',string2)
print(result2)

