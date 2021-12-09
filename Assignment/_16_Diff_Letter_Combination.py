# Create and display all combinations of letters, selecting each letter from a different key in a dictionary
from itertools import product
class LettersCombination:
        def __init__(self, size):
            self.size = size
            self.ipdict = {}
            i = 0
            while i < self.size:
                self.dict_creation()
                i += 1
            print(self.ipdict)
            self.combinationLetters()

        def dict_creation(self):
            keyno = int(input("Enter key:"))
            self.valueno_list = []
            self.no_values = int(input("Enter total no. of values of {} key".format(keyno)))
            for i in range(0,self.no_values):
                valueno = input("Enter value:")
                self.valueno_list.append(valueno)
            self.ipdict[keyno] = self.valueno_list
        """
        def combinationLetters(self):
            self.opdict = sorted(self.ipdict.items(), key = lambda x:x[0])
            print(self.opdict)
            #{1: ['a', 'b']}
            #[(1, ['a', 'b'])]
            for item in range(0,self.size):
                print(self.opdict[item][1])
        """
        def combinationLetters(self):
            for val1,val2 in product(*self.ipdict.values()):
                    print(val1 + val2)

size = int(input("Enter size of dictionary > 1:"))
obj = LettersCombination(size)


