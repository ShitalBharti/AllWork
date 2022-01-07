# Insert a given string at the beginning of all items in a list

class InsertString:

    def __init__(self,str1):
        self.string = str1
        self.lst = [1,2,3]

    def insert(self):
        self.lst.insert(0,self.string)
        print(self.lst)

string = input("Enter String: ")
ins = InsertString(string)
ins.insert()
