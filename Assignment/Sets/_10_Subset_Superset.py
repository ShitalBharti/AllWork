class SubsetSuperset:
    def __init__(self):
        self.setA = {1,2,3,4,5,6,7,8,9}
        self.setB = {1,2,3,4,5,6}
        self.setC = {1,2,3,4,5}
        print("Set A:{} \nSet B:{} \nSet C:{}".format(self.setA,self.setB,self.setC))
        self.checkSuperset()
        self.checkSubset()

    # Using built-in function -> Superset
    def checkSuperset(self):
        print("--------------------------Superset--------------------------------")
        print("A superset B:",self.setA.issuperset(self.setB))
        print("B superset A:",self.setB.issuperset(self.setA))
        print("A superset C:",self.setA.issuperset(self.setC))
        print("B superset C:",self.setB.issuperset(self.setC))
        print("C superset A:",self.setC.issuperset(self.setA))
        print("C superset B:",self.setC.issuperset(self.setB))

    # Using built-in function - Subset
    def checkSubset(self):
        print("--------------------------Subset--------------------------------")
        print("A subset B:", self.setA.issubset(self.setB))
        print("B subset A:", self.setB.issubset(self.setA))
        print("A subset C:", self.setA.issubset(self.setC))
        print("B subset C:", self.setB.issubset(self.setC))
        print("C subset A:", self.setC.issubset(self.setA))
        print("C subset B:", self.setC.issubset(self.setB))


obj = SubsetSuperset()


