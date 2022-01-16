class MoveZeroes:
    def userInput(self):
        self.nums = []
        self.n = int(input("Enter size of list: "))
        for i in range(self.n):
            element = int(input("Enter element: "))
            self.nums.append(element)
        print(self.nums)
        self.moveZeroes()

    def moveZeroes(self):
        for i in range(self.n):
            for j in range(self.n-1):
                if self.nums[j] == 0:
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j+1]
                    self.nums[j+1] = temp
        print(self.nums)

movez = MoveZeroes()
movez.userInput()