# Split a list every Nth element

class SplitList:
    def __init__(self,n):
        self.list1 = [1,2,3,4,5,6,7,8,9,10]
        self.n = n
        self.oplist = []

    def split(self):
        i = 0; pos = self.n
        while i < len(self.list1):
            self.oplist.append(self.list1[i:pos])
            i = pos
            pos += self.n

        print(self.oplist)

n = int(input("Enter position: "))
splitobj = SplitList(n)
splitobj.split()
