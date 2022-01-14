
class CheckUgly:

    def __init__(self,num):
        self.num = num
        self.primelst = [2, 3, 5]

    def factors(self):
        if num > 1:
            self.flst = []
            for i in range(2,num):
                if num % i == 0:
                    self.flst.append(i)
            print(self.flst)

    def checkPrime(self):
        self.pflst = []
        flag = False
        for element in self.flst:
            for i in range(2,int(element/2)+1):
                if element % i == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag == True or element in self.primelst:
                self.pflst.append(element)
        print(self.pflst)

    def checkUglyNum(self, flag = False):
        if self.num == 1 or self.num in self.primelst:
            return True
        else:
            self.factors()
            self.checkPrime()
            for element in self.pflst:
                if element in self.primelst:
                    flag = True
                else:
                    flag = False
                    break
        return flag

num = int(input("Enter number: "))
ugly = CheckUgly(num)
val = ugly.checkUglyNum()
print(val)

