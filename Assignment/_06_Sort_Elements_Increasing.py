class SortElements:
    def __init__(self,size):
        self.size = size
        self.iplist = []
        print("Only Enter Integer Values:")
        i = 0
        while i < self.size:
            try:
                self.list_creation()
            except:
                print("Only Enter Integer Values")
                i -= 1
                print(i)
            i += 1
        print("Original List:",self.iplist)
        self.sortElements()

    def list_creation(self):
        element = int(input("Enter element:"))
        self.iplist.append(element)

    def sortElements(self):
        self.iplist.sort()
        print("Sorted List:",self.iplist)

size = int(input("Enter size:"))
obj = SortElements(size)


