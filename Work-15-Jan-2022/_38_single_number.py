'''Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.'''
class Solution():
    def singleNumber(self, nums):
        dict = {}
        if ( nums == [] ):
            return -1
        for d in nums:
            if d in dict:
                del dict[d]
            else:
                dict[d] = 1
        return list(dict.keys())
nums=[2,5,2,2,2,5,8,8,3,6]
s=Solution()
print(s.singleNumber(nums))