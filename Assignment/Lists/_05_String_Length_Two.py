class StringLength:
    def user_input(self):
        self.iplist = []
        self.size = int(input("Enter size of list:"))
        for i in range(0,self.size):
            element = input("Enter element:")
            self.iplist.append(element)
        self.stringLengthTwo()

    def stringLengthTwo(self):
        count = 0
        for i in range(0,self.size):
            if self.iplist[i].isalpha():
                if len(self.iplist[i]) == 2:
                    count = count + 1
        print("Total no. of strings are:{}".format(count))

obj = StringLength()
obj.user_input()
