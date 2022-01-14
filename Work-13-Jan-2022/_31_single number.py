#single number
def single_number(nums):
    a=0
    for i in nums:
        a^=i
    return a
#a=a^i
#we can juse xor all bits together to find the unique number
s1=single_number(nums=[1,8,9,8,9,1,7])
print(s1)