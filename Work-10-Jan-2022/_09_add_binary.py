#here we are taking the numbers in binary format thats why giving strings format
#because if we give in 111 in format .. it will consider as integer
first_number='111'
second_number='001'
#binary=2#that's why we put 2
sum=bin(int(first_number,2)+int(second_number,2))
print(sum)#0b1000
#to get only output we are taking slicing
print(sum[2:])