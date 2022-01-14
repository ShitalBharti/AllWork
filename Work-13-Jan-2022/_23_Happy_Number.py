class HappyNumber:

    def checkHappy(self,num,add = 0):
        if num == 1:
            return True
        else:
            try:
                self.digit = []
                while num != 0:
                    rem = int(num % 10)
                    self.digit.append(rem)
                    num = int(num / 10)
                return self.squareDigit()
            except:
                return False

    def squareDigit(self,add = 0):
        for element in self.digit:
            sqr = element * element
            add = add + sqr
        num = add
        return self.checkHappy(num)

n = int(input("Enter number: "))
happy = HappyNumber()
res = happy.checkHappy(n)
print(res)

