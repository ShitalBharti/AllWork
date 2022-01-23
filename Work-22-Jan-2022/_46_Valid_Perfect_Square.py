class PerfectSquare:
    def userinput(self):
        self.num = int(input("Enter integer no: "))

    def check(self):
        factorlst = []
        for i in range(2,self.num):
            if self.num % i == 0:
                factorlst.append(i)
        print(factorlst)
        for item in factorlst:
            if item * item == self.num:
                return True
        return False

ps = PerfectSquare()
ps.userinput()
res = ps.check()
print(res)
