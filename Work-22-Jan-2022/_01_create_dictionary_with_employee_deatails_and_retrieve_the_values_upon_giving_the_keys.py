'''create dictionary with emplyee details and retrive the values upon giving the keys'''
#creating dictionary with key value pairs
dict1={"name":"rakshitha","id":55,"salary":25000}
#acess value by giving key
print('Name of the employee ',dict1['name'])
print('id of the employee ',dict1['id'])
print('salary of the employee',dict1['salary'])
n=len(dict1)
print(n)
dict1['salary']=10000
print(dict1)
dict1['dept']='finance'
print(dict1)
del dict1['id']
print(dict1)
print('dept' in dict1)
print('gender' in dict1)
emp={'Nag':10,'vishnu':20,'Nag':30}
print(emp)
emp={['nag']:10,'vishnu':20,'Raj':30}
print(emp)
'''dictionary methods
1. clear()--> d.clear()-->Removes all key value pair from dictionary
2. copy()--> d1=d.copy()-->copies all element from 'd' into a new dictionary'd1'
3. fromkeys()-->d.fromkeys(s[,v])-->create a new dictionary with key from sequence 's' and return values all set to 'v'
4. get()-->d.get(k[,v])-->Returns the value associated with key 'k'.if not found,it returns v
5. items()-->d.items()-->Reurns an object that contains key-value pairs of'd'.the pairs are stored as tuples in the object
6. keys()-->d.keys()-->Returns a sequence of keys from the dictionary'd'
7. values()-->d.values()-->Returns a sequence of values from the dictionary 'd'
8. update()--> d.update(x)-->adds all element from dictionary'x' to 'd'
9. pop()-->d.pop(k[,v])-->removes the key 'k' and its value from 'd' and returns the value.if key
 is not found,then the value'v' is returned.if key is not found and 'v' is not mentoned then 'keyerror' raised
10. setdefault()-->d.setdefault(k[,v])--> If key 'k' is found its value is returned.if key is not found then the 
k,v pair is stored into the dictionary'd'




'''