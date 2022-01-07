# Find a tuple, the smallest second index value from a list of tuples

class SmallestValue:
    def __init__(self):
        self.lst_tup = [(1,1,3),(4,1,3),(5,6)]

    def findValue(self):
        self.oplst = []
        for element in self.lst_tup:
            temp = element[1]
            self.oplst.append(temp)
        val = min(self.oplst)
        for element in self.lst_tup:
            if val == element[1]:
                print(element)

smaller = SmallestValue()
smaller.findValue()
