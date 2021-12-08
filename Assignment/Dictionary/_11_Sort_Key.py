class SortKeys:
    def __init__(self,size):
        self.size = size
        self.ipdict = {}
        i = 1
        while i <= self.size:
            self.user_input()
            i += 1
        self.sortingKey()

    def user_input(self):
        keyno = int(input("Enter key:"))
        valueno = int(input("Enter value:"))
        self.ipdict[keyno] = valueno

    def sortingKey(self):
        print("Sorted dictionary is:")
        for i in sorted(self.ipdict):
            print((i, self.ipdict[i]), end=" ")

size = int(input("Enter size of dictionary:"))
obj = SortKeys(size)


