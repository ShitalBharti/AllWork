#  Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.

class SubsetSuperset:
    def __init__(self):
        self.setA = {1,2,3,4,5,6,7,8,9}
        self.setB = {1,2,0,4,7,6}
        print("Set A:{} \nSet B:{}".format(self.setA,self.setB))
        self.shallowCopy()

    # Using built-in function -> copy
    def shallowCopy(self):
        setC = self.setA.copy()
        setD = self.setB.copy()
        print("Set C:{} \nSet D:{}".format(setC,setD))

obj = SubsetSuperset()
