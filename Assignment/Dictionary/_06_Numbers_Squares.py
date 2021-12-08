class KeysSquares:
    def __init__(self,size):
        self.size = size
        self.squaredict = {}
        self.opdict = {}
        i = 1
        while i <= self.size:
            self.user_input()
            i += 1
        print(self.squaredict)
        self.findPairs()

    def user_input(self):
        keyno = int(input("Enter key:"))
        valueno = int(input("Enter value:"))
        self.squaredict[keyno] = valueno

    def findPairs(self):
        for i,j in self.squaredict.items():
            if i * i == j:
                self.opdict[i] = j
        print(self.opdict)

size = int(input("Enter size of dictionary:"))
obj = KeysSquares(size)


