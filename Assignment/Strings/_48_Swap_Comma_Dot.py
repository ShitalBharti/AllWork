class SwapCommaDot:
    def user_input(self):
        self.string = input("Enter string:")
        self.output = ''
        self.swaping()

    def swaping(self):
        for char in self.string:
            if char == '.':
                self.output = self.output + ','
            elif char == ',':
                self.output = self.output + '.'
            else:
                self.output = self.output + char
        print(self.output)

obj = SwapCommaDot()
obj.user_input()

