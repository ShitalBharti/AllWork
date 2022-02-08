class ThreeSum:

    def user_input(self):
        self.numlst = [int(x) for x in input("Enter integer element: ").split(',')]
        print(self.numlst)
        self.checkSum()

    def checkSum(self):
        length = len(self.numlst)
        oplst = []
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    total = self.numlst[i]+self.numlst[j]+self.numlst[k]
                    res = [self.numlst[i],self.numlst[j],self.numlst[k]]
                    print("{} == {}".format(res,total))
                    if total == 0:
                        res = sorted(res)
                        if res not in oplst:
                            oplst.append(res)
        print(oplst)


tsum = ThreeSum()
tsum.user_input()


