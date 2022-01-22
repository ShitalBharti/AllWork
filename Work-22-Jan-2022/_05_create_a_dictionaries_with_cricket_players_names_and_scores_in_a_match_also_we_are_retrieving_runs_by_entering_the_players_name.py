'''create a dictionary with cricket players names and scores'''
x={}
n=int(input("enter the no. of key value pair : "))
for i in range(n):
    k=input("enter the key :")
    v=int(input("enter the value:"))
    x.update({k:v})
print("the dictionary is: ",x)
#diplay only player names
for i in x.keys():
    print(i)
#accept player name from the dictionary
n=int(input("enter the size of the playes :"))
for i in range(n):
    k=input("enter the player name :")
    v= input("enter the player score :")
    x.update({k:v})
print(x)
#accept a player name from keyboard
name=input("enter the player name :")
#find the runs done by teh player
runs=x.get(name,-1)
if(runs==-1):
    print("players not found")
else:
    print('{} made runs {}.'.format(name,runs))

