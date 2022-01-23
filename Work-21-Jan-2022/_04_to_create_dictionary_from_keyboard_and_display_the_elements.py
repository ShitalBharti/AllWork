x={}
#print('how many elments? ',end='')
n=int(input("enter the number of key-value pair"))
for i in range(n):
    #print('enter key :',end='')
    k=input()
    #print('enter its value: ',end='')
    v=int(input())
    x.update({k:v})
print('the dictionary is :',x)