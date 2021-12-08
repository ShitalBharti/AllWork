class CommaSeparator:
    def user_input(self):
        self.string = input("Enter number:")
        if self.string.isdigit() == True:
            self.commaSeparated()
        else:
            print("Invalid number!")
            exitwindow = input("Print Bye to exit! or any key to continue!").lower()
            if exitwindow == 'bye':
                exit()
            else:
                self.user_input()

    # Main logic starts from here
    def commaSeparated(self):
        output = ''
        length = len(self.string)
        for char in range(length):
            if char == length - 1:
                output = output + self.string[char]
            else:
                output = output + self.string[char] + ','
        print("Comma Separated String is: {}".format(output))

obj = CommaSeparator()
obj.user_input()