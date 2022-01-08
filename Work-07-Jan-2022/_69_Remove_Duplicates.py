# Remove duplicates from a list of lists

'''

import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)

'''
import itertools


class RemoveDuplicates:

    def __init__(self):
        self.numlst = [[10,20,20],[40,40],[30,56,25],[10,20],[40],[33]]
        print('Origina list:',self.numlst)

    def removeDup(self):
        newlst = []

        # to remove duplicates from elements which are list
        for element in self.numlst:
            temp = set(element)
            item = list(temp)
            newlst.append(item)
        print(newlst)

        # to remove duplicate elements
        for element in newlst:
            if newlst.count(element) > 1:
                newlst.remove(element)

        print(newlst)

    def groupby(self):
        print("---------------------------built-in module------------------")
        self.numlst.sort()
        new_num = list(num for num, _ in itertools.groupby(self.numlst))
        print("New List", new_num)



rd = RemoveDuplicates()
rd.removeDup()
rd.groupby()
