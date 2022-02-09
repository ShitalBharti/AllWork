
class PalindromicNumber:
    def largestPalindrome(self):
        self.innum = int(input("Enter number:(at least 2 digits) "))
        digit = 0
        temp = self.innum

        # checking the digits
        while temp > 0:
            temp = int(temp/10)
            digit += 1
        if digit >= 2:
            self.findPermutations()
        else:
            self.largestPalindrome()

    def findPermutations(self):
        self.numlst = []
        temp = self.innum

        #storing digits in list
        while temp > 0:
            rem = int(temp%10)
            temp = int(temp/10)
            self.numlst.append(rem)

        self.oplst = []
        self.printPermutations(self.numlst,0)

    # recursive function to find all permutations
    def printPermutations(self,numlst, cid):

        if cid == len(numlst):
            # print(numlst)
            strnum = ''
            for ele in numlst:
                ele = str(ele)
                strnum = strnum + ele
            if strnum == strnum[::-1]:  #to check palindrome string
                self.oplst.append(int(strnum))
        i = cid
        while i<len(numlst):
            numlst = self.swap(numlst,i,cid)
            self.printPermutations(numlst,cid+1)
            numlst = self.swap(numlst,i,cid)
            i += 1

    def swap(self,numlst,i,j):
        temp = numlst[i]
        numlst[i] = numlst[j]
        numlst[j] = temp
        return numlst

    def maxPalindrome(self):
        if self.oplst == []:
            print(-1)
        else:
            print("All Palindromic permuations are: ")
            print(self.oplst)
            print("Maximum is ",max(self.oplst))


pno = PalindromicNumber()
pno.largestPalindrome()
pno.maxPalindrome()



