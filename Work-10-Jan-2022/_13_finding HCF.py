#HCF:highest common factor/greatest common factor (gcf)
'''first=int(input('enter the first number:'))
#second=int(input('enter the second number:'))
first_list=[]
#initially finding the smallest numbers factors
for i in range(1,first+1):
    if first%i==0:
        first_list.append(i)
print(first_list)'''


'''highest common factor:
60:2x30,2x15,3x5,5x1:2,2,3,5,1
72:2x2x2x3x3x1
CF=2x2x3x1
HCF=2x2x3x1=12'''


def findgcd(number1,number2):
    if number1>number2:
        small_number=number2
    else:
        small_number=number1
    for i in range(1,small_number+1):
        if (number1%i==0) and (number2%i==0):
            result=i
    return result

number1=60
number2=72
ans=findgcd(number1,number2)
print(ans)

