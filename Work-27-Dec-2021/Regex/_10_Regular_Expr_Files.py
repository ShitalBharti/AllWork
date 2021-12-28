# to read email-ids from a text file

import re
import urllib.request

f = open('mails.txt','r')

for line in f:
    res = re.findall(r'\S+@\S+',line)

if len(res)>0:
    print(res)

f.close()

# to retrieve data from a file and then write data into a file.

f1 = open('salaries.txt','r')
f2 = open('newfile.txt','w')

for line in f1:
    res1 = re.search(r'\d{4}',line)
    res2 = re.search(r'\d{4,}.\d{2}',line)
    print(res1.group(),res2.group())
    f2.write(res1.group())
    f2.write(res2.group())
f1.close()
f2.close()

# to retrieve information from HTML file using a regular expression.

f = urllib.request.urlopen(r'file:///f|py\breakfast.html')  # open html file
text = f.read() # read data of file
string = text.decode()  # convert byte string into normal string
result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d\d.\d\d)</td>',string)
print(result)
for item, price in result:
    print('Item = %-15s Price = %-10s' %(item,price))
f.close()


