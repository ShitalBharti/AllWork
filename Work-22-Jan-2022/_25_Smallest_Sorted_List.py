class SmallestSorted:
    def userInput(self):
        n = int(input("Enter size of sorted list: "))
        self.nums = []
        for i in range(0, n):
            element = int(input("Enter element: ")) # 0 1 2 4 5 6 7 8
            self.nums.append(element)
        self.smallestSorted()

    def smallestSorted(self):
        print(self.nums)

        self.oplst = []
        for element in self.nums:
            if self.nums.index(element) == 0:
                rang = []
                curr = element
                rang.append(curr)
            else:
                nxt = element
                if nxt == curr+1:
                    rang.append(nxt)
                    curr = nxt
                else:
                    self.oplst.append(rang)
                    curr = element
                    rang = []
                    rang.append(curr)
            #print(rang)
        self.oplst.append(rang)
        print(self.oplst)


lst = SmallestSorted()
lst.userInput()



