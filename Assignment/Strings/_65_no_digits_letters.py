class CountDigitLetter:
    def user_input(self):
        self.string = input("Enter String")
        self.countDig_Let()

    def countDig_Let(self):
        count = 0
        count1 = 0
        for i in self.string:
            if i.isdigit():
                count += 1
            elif i.isalpha():
                count1 += 1
            else:
                pass
        print("-------------Using For Loop--------------------")
        print("the no of chars is", count1, "and the number of digits is", count)

obj = CountDigitLetter()
obj.user_input()
