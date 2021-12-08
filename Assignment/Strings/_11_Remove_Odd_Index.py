class RemoveOddIndex:
    def removeOdd(self):
        str = input("enter your string:")
        res = ""
        for i in range(len(str)):
            if i % 2 == 0:
                res = res + str[i]
        print("After Removing Odd Index:",res)

obj = RemoveOddIndex()
obj.removeOdd()

