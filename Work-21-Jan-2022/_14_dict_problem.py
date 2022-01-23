'''Write a program to enter name and percentage marks in a dictionary and
display information on the screen
'''
dict1={}
n=int(input("enter the number of key value pair"))
i=1
while i<=n:
    key=input("enter the keys")
    value=int(input("enter the values"))
    dict1[key]=value
    i+=1
print(dict1)