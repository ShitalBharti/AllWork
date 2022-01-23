#396. Rotate Function
#rotate the array and multipl with its base value


num=[1,2,3,4,5]
max1=0
for j in range(len(num)):
    total=0
    for i in range(len(num)):
        total=total+num[i]*i
    print(total)
    num=num[1:]+num[:1]
    max1=max(total,max1)
print("--------------------")
print(max1)
