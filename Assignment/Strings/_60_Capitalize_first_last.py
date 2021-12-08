class CapitalizeFirstLetter:
    def user_input(self):
        self.string = input("Enter string:")
        print("Entered string is:\'{}\'".format(self.string))
        self.FirstLetterWordCapitalize()

    def FirstLetterWordCapitalize(self):
        output_list = []
        list_words = self.string.split(' ')
        for word in list_words:
            if word != '':
                output_list.append(word.capitalize())
        print(output_list)

obj = CapitalizeFirstLetter()
obj.user_input()
