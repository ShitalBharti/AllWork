# Create a list with infinite elements

class CreateInfiniteList:
    def __init__(self):
        self.list = []

    def createList(self):
        while True:
            x = input("Enter Element: ")
            self.list.append(x)
            print(self.list)

infinite = CreateInfiniteList()
infinite.createList()