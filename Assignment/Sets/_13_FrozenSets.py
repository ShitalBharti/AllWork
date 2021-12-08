"""
-> The frozenset() is an inbuilt function in Python which takes an iterable object as input and makes them immutable.
-> Simply it freezes the iterable objects and makes them unchangeable.
-> frozensets are immutable which means that elements from the frozenset cannot be added or removed once created.
-> This function takes input as any iterable object and converts them into an immutable object. The order of elements is not guaranteed to be preserved.
-> Since frozenset object are immutable they are mainly used as key in dictionary or elements of other sets.
"""
class FrozenSets:
    def __init__(self):
        self.setA = {1,2,3,4,5,6,7,8,9}
        self.setB = {1,2,3,4,5,6}
        self.setB = frozenset(self.setB)
        print("Set A:{} \nSet B:{}".format(self.setA,self.setB))
        self.udOperationsSet()

    def udOperationsSet(self):
        print("--------------NormalSet(Mutable)------------------------")
        self.setA.add(10)
        self.setA.remove(7)
        print("Set A:{}".format(self.setA))

        print("--------------FrozenSet(Immutable)------------------------")
       # self.setB.add(10)  # -> Runtime Error
       # self.setB.remove(7) # -> Runtime Error
        print("Set B:{}".format(self.setB))

obj = FrozenSets()
