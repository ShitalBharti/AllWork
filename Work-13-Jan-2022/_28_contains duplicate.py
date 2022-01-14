def contains_duplicate(nums):
    s=set()
    for ele in nums:
        if ele in s:
            return True
        else:
            s.add(ele)
            return False
s1=contains_duplicate(nums=[1,2,3,4])
print(s1)



