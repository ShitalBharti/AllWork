class Longest_Word:
    def __init__(self):
        try:
            self.size = int(input("Enter size:"))
            self.iplist = []
            self.list_creation()
            self.longWord()
        except:
            print("Enter size as postive no")
            self.__init__()

    def list_creation(self):
        for i in range(0,self.size):
            element = input("Enter element:")
            self.iplist.append(element)
        print("Input List:",self.iplist)

    def longWord(self):
        max_len = 0
        for element in self.iplist:
            length = len(element)
            if max_len <= length:
                if max_len != length:
                    long_word_list = []
                    long_word_list.append(element)
                else:
                    long_word_list.append(element)
                max_len = length
        print(long_word_list)

obj = Longest_Word()


