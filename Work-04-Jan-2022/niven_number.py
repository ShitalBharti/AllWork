print("****find the given number is niven number*****")
num=int(input("enter the number"))
str=str(num)
sum=0
for i in str:
    sum=sum+int(i)

res=num%sum
if res==0:
    print(f'{num} is niven number')
else:
    print(f'{num}is not niven number')