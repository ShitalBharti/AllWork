class ReverseString:
    def user_input(self):
        self.string = input("Enter string:")
        self.reverseString()
        self.reverseStringList()

    # Using while loop
    def reverseString(self):
        reverse = ''
        length = len(self.string)
        value = -length
        i = -1
        while i >= value:
            reverse = reverse + self.string[i]
            i = i - 1
        print("----------------Using While Loop---------------------")
        print("Reverse String:",reverse)

    # Using list
    def reverseStringList(self):
        list_str = list(self.string)
        opstring = ''
        print("----------------Using Lists method---------------------")
        list_str.reverse()
        for item in list_str:
            opstring = opstring + item
        print("Reverse String:",opstring)

obj = ReverseString()
obj.user_input()



