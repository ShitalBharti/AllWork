# Convert a string to a list

class StringToList:

    def __init__(self, str1):
        self.string = str1

    def convert(self):
        lst = []
        for char in self.string:
            lst.append(char)

        print(lst)

string = input("Enter String: ")
strlist = StringToList(string)
strlist.convert()
