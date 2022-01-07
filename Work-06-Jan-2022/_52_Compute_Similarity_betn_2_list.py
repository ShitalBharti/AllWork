
class ComputeSimilarity:
    def __init__(self):
        self.list1 = [1, 4, 6, 8, 9, 10, 7]
        self.list2 = [7, 11, 12, 8, 9]
        self.sim_lst = []

    def findSimilar(self):
        for element in self.list1:
            if element in self.list2:
                self.sim_lst.append(element)

        print(self.sim_lst)

similar = ComputeSimilarity()
similar.findSimilar()