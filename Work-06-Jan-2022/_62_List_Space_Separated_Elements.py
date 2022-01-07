# Print a list of space-separated elements

class SpaceSeparated:

    def userInput(self):
        print("Enter elements space separated: ")
        self.list1 = [x for x in input().split()]
        print(self.list1)


space = SpaceSeparated()
space.userInput()