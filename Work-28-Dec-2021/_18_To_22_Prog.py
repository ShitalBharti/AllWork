# Combine values in python list of dictionaries.
print("------------------------combine values in list-------------------")
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result=Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)

# Create a dictionary from a string
print("------------------------dict from string-------------------")
str1="shital"
mydict={}
for i in str1:
    mydict[i]=mydict.get(i,0)+1
print(mydict)

# Print a dictionary in table format.
print("------------------------dict in table format-------------------")
dict1={}
dict1={(0, 0): 'Samuel', (0, 1): 21, (0, 2): 'Data structures',
         (1, 0): 'Richie', (1, 1): 20, (1, 2): 'Machine Learning',
         (2, 0): 'Lauren', (2, 1):21, (2, 2): 'OOPS with Java'}
print("NAME","AGE","COURSE")
for i in range(3):
    for j in range(3):
        print(dict1[(i,j)],end='  ')
    print()

# Count the values associated with key in a dictionary
print("------------------------count values associated with key-------------------")
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))

# Convert a list into a nested dictionary of keys.
print("------------------------list to dict-------------------")
list=[1,2,3,4,5,6]
dict1=current=  {}
for i in list:
    current[i]={}
    current=current[i]
print(dict1)
