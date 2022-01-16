class WordPattern:
    def userInput(self):
        self.pattern = input("Enter pattern string: ")
        self.s = input("Enter string to check: ")
        self.snospaces = self.s.strip()
        print(self.snospaces)

    def checkPattern(self):
        dictPattern = {}
        slst = list(self.snospaces.split())
        print(slst)
        flag = False
        if len(self.pattern) == len(slst):
            for index in range(len(self.pattern)):
                if self.pattern[index] in dictPattern.keys():
                   if dictPattern.get(self.pattern[index]) == slst[index]:
                       flag = True
                   else:
                       return False
                else:
                    dictPattern[self.pattern[index]] =  slst[index]
            if flag == True:
                print(dictPattern)
                return True
        else:
            return False

wordp = WordPattern()
wordp.userInput()
result = wordp.checkPattern()
print(result)