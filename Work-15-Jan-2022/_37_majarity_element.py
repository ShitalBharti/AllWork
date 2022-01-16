'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.'''
class Solution:
    def majorityElement(self, nums):
        candi, count = 0, 0
        for num in nums:
            if count == 0:
                candi = num
                count += 1
            elif num == candi:
                count += 1
            else:
                count -= 1
        return candi

nums=[4,8,5,7,7,7,7,23]
s=Solution()
print(s.majorityElement( nums))