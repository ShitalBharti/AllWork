'''Issubset and issuperset'''
class Set:
    def issubset1(self,lst1,lst2):
        try:
            self.lst1=lst1
            self.lst2=lst2

            print(lst1.issubset(lst2))
            print(lst2.issubset(lst1))
            print(lst1.issuperset(lst2))
            print(lst2.issuperset(lst1))
        except Exception as e:
            print("give a valid input",e)   # ---> iF INPUT GIVEN IS SOMETHING ELSE NOT SET

lst1=[1,2,3,4,5,5]
lst2={1,2,3,4}

obj=Set()
output=obj.issubset1(lst1,lst2)