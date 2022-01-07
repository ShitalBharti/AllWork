# Check if all items of a list is equal to a given string

class ItemInList:

    def __init__(self, str1):
        self.string = str1
        self.lst = []
        for i in range(0,15):
            char = chr(97 + i)
            self.lst.append(char)
        print(self.lst)

    def check(self):
        flag = False

        for char in self.string:
            if char in self.lst:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            print("All present")
        else:
            print("Not present")

string = input("Enter String: ")
itemlist = ItemInList(string)
itemlist.check()