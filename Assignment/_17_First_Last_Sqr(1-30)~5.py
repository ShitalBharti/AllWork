class SquaresExFirstFive:
    def __init__(self):
        try:
            self.size = int(input("Enter size:"))
            self.iplist = []
            self.list_creation()
            self.squaresFind()
        except:
            print("Enter size as postive no")
            self.__init__()

    def list_creation(self):
        i = 0
        while i < self.size:
            try:
                element = int(input("Enter element:"))
                self.iplist.append(element)
            except:
                print("Only Enter Integer Values")
                i -= 1
            i += 1
        print("Input List:",self.iplist)

    def handle_return(self):
        first = self.squaresFind()
        self.iplist.sort(reverse=True)
        last = self.squaresFind()
        return [first,last]

    def squaresFind(self):
        for item in range(6,self.size):
            if self.iplist[item] < 6:
                sqr1 = self.iplist[item] * self.iplist[item]
                if 1 <= sqr1 <= 30:
                    found = self.iplist[item]
                    break
        return found

obj = SquaresExFirstFive()
res = obj.handle_return()
if res[0] == res[1]:
    print("First Element:", res[0])
else:
    print("First Element:", res[0])
    print("Last Element:", res[1])