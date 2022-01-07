# Concatenate elements of a list

class ConcatenateElements:
    def __init__(self):
        self.list1 = ['a','b','c','d','e']
        self.list2 = ['f','g','h','i','j']
        self.oplist = []

    def cocatenate(self):
        for element in self.list2:
            self.list1.append(element)
        print(self.list1)

concat = ConcatenateElements()
concat.cocatenate()
