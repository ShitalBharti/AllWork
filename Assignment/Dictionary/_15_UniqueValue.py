class UniqueValues:
    def __init__(self,size):
        self.size = size
        self.ipdict = {}
        self.oplist = []
        i = 1
        while i <= self.size:
            self.user_input()
            i += 1
        self.printUniqueValues()

    def user_input(self):
        keyno = int(input("Enter key:"))
        valueno = int(input("Enter value:"))
        self.ipdict[keyno] = valueno

    def printUniqueValues(self):
        print("Unique values in dictionary:")
        for j in self.ipdict.values():
            self.oplist.append(j)
        self.oplist = set(self.oplist)
        print(self.oplist)

size = int(input("Enter size of dictionary:"))
obj = UniqueValues(size)
