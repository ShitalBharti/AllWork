from itertools import permutations

class NextPermutation:

    def nextPermutation(self):
        self.numlst = [int(x) for x in input("Enter integers (,) ").split(",")]
        print(self.numlst)
        oplst = list(permutations(self.numlst))
        print(oplst)
        self.finallst = []
        for element in oplst:
            op = self.stringConvert(element)
            self.finallst.append(op)
        print(self.finallst)

    def stringConvert(self,inlst):
        strdig = ''
        for element in inlst:
            strdig = strdig + str(element)
        check = int(strdig)
        return check

    def findClosest(self):
        temp = self.stringConvert(self.numlst)
        print(temp)
        diffdict = {}
        for element in self.finallst:
            if element == temp:
                continue
            else:
                diffdict[element] = element - temp

        minval = min(diffdict.values())
        for key in diffdict.keys():
            if diffdict.get(key) == minval:
                ans = key
        print(ans)

np = NextPermutation()
np.nextPermutation()
np.findClosest()