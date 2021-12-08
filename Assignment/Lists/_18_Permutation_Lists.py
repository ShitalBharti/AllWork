import itertools

class PermutationList:
    def user_input(self):
        self.iplist = []
        self.size = int(input("Enter size of list:"))
        for i in range(0, self.size):
            element = input("Enter element:")
            self.iplist.append(element)
        self.possiblePermutation(self.size)

    def possiblePermutation(self,size):
        oplist = []
        for rep in range(2,size+1):
            oplist = oplist + list(itertools.permutations(self.iplist,rep))
        print(oplist)
        print(len(oplist))

obj = PermutationList()
obj.user_input()