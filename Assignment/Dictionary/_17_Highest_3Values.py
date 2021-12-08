class HighestValues:
    def __init__(self,size):
        self.size = size
        self.ipdict = {}
        self.oplist = []
        i = 1
        while i <= self.size:
            self.user_input()
            i += 1
        self.printHighestValues()

    def user_input(self):
        keyno = int(input("Enter key:"))
        valueno = int(input("Enter value:"))
        self.ipdict[keyno] = valueno

    def printHighestValues(self):
        print("Highest 3 values in dictionary:")
        for j in self.ipdict.values():
            self.oplist.append(j)
        self.oplistset = set(self.oplist)
        self.oplist = list(self.oplistset)
        self.oplist.sort()
        print({self.oplist[2], self.oplist[1], self.oplist[0]})


size = int(input("Enter size of dictionary:"))
obj = HighestValues(size)
