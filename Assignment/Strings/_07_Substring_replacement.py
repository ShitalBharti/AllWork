class SubstringReplace:

    def user_input(self):
        self.string = input("Enter String:")
        self.sub = input("Enter Substring:")
        self.replace()

    def replace(self):
        if self.string.find(self.sub) == 1:
            self.rep_string = input("Enter replace string:")
            print(self.string.replace(self.sub, self.rep_string))
        else:
            print("Enter valid substring!")
            self.user_input()

obj = SubstringReplace()
obj.user_input()
