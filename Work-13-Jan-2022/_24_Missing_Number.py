class MissingNumber:
    def missingNumber(self,nums):
        print(nums)
        newlst = []
        length = len(nums)
        for i in range(0,length+1):
            newlst.append(i)
        for element in newlst:
            if element not in nums:
                print(element)


size = int(input("Enter length of array: "))
numlst = []
for i in range(size):
    element = int(input("Enter no: "))
    numlst.append(element)
mno = MissingNumber()
mno.missingNumber(numlst)


