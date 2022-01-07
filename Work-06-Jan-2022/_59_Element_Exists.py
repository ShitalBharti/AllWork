# Check if the n-th element exists in a given list

class ElementExist:
    def __init__(self,n):
        self.lst = [1, 2, 3, 4, 5]
        print(self.lst)
        self.n = n

    def check(self):
        if self.n in self.lst:
            print('Present')
        else:
            print("Not Present")

n = int(input("Enter Element"))
el = ElementExist(n)
el.check()
