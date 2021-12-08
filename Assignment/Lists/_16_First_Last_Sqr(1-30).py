class Squares:
    def user_input(self):
        self.iplist = []
        self.size = int(input("Enter size of list:"))
        for i in range(0, self.size):
            element = int(input("Enter element:"))
            self.iplist.append(element)
        first = self.squaresFind()
        self.iplist.sort(reverse=True)
        last = self.squaresFind()
        return [first,last]

    def squaresFind(self):
        for item in range(0,self.size):
            if self.iplist[item] < 6:
                sqr1 = self.iplist[item] * self.iplist[item]
                if 1 <= sqr1 <= 30:
                    found = self.iplist[item]
                    break
        return found

obj = Squares()
res = obj.user_input()
if res[0] == res[1]:
    print("First Element:", res[0])
else:
    print("First Element:", res[0])
    print("Last Element:", res[1])