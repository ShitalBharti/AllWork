list1=[]
number=int(input('Enter a number:'))
for i in range(1,number+1):
    if number%i==0:
        list1.append(i)
print(list1)

#to get square root.. but answers will be integers only
number=int(input('Enter a number:'))
for i in range(1,number+1):
    if number%i==0:
        print(i)
        if i*i==number:
            print('square root',i)