class LongestWord:
    def user_input(self):
        self.string = input("Enter String:")
        self.calculateLength()

    def calculateLength(self):
        list_words = self.string.split(' ')
        max_len = 0
        for item in list_words:
            length = len(item)
            if max_len <= length:
                if max_len != length:
                    long_word_list = []
                    long_word_list.append(item)
                else:
                    long_word_list.append(item)
                max_len = length
        print(long_word_list)

obj = LongestWord()
obj.user_input()