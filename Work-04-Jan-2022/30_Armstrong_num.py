print("Python Program to Check Armstrong Number")
print("Armstrong number: the sum of cubes of each digit is equal to the number itself.")

num=int(input("enter the number"))
sum=0

temp=num
while temp>0:
      digit=temp%10
      sum +=digit**3
      temp=temp//10

if sum==num:
   print(f"{sum } is an Armstrong number")
else:
    print(f"{sum} is not  an Armstrong number")