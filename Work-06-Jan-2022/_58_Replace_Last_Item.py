# Replace the last element in a list with another list

class ReplaceLast:

    def __init__(self):
        self.lst = [1,2,3,4,5]
        self.rep = [6,7,8]

    def replace(self):
        self.lst.pop()
        self.lst.append(self.rep)
        print(self.lst)

rep = ReplaceLast()
rep.replace()