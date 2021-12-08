class Characters:
    def user_input(self):
        self.string = input("Enter String:")
        self.charToList()

    def charToList(self):
        oplist = []
        for char in self.string:
            oplist.append(char)
        print(oplist)

obj = Characters()
obj.user_input()

