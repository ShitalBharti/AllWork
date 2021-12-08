class StringList:
        def user_input(self):
                self.string = input("Enter string:")
                self.conversion()

        def conversion(self):
                list1 = []
                for i in range(len(self.string)):
                        list1.append(self.string[i])
                print(list1)

obj = StringList()
obj.user_input()