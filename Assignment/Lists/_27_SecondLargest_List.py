class SecondLargestNumber:
    def user_input(self):
        self.iplist = []
        size = int(input("Enter size of list:"))
        i = 0
        while i < size:
            try:
                element = int(input("Enter integers:"))
                self.iplist.append(element)
            except:
                print("Enter integers only!")
                i = i - 1
            i = i + 1
        self.methodList()

    def methodList(self):
        print("List:",self.iplist)
        self.iplist.sort(reverse=True)
        print("Second Largest element in list is: {}".format(self.iplist[1]))

obj = SecondLargestNumber()
obj.user_input()