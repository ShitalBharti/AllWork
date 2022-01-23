#converting a string into a dictionary
str="rakshitha=45,varun=95,vinith=96,deekshith=56"
#brake the string at',' and then at'=' store the pieces into a list list
lst=[]
for x in str.split(','):
    y=x.split('=')
    lst.append(y)
d=dict(lst)
print(d)
d1={}
for k,v in d.items():
    d1[k]=int(v)
print(d1)