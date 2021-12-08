class DictCreation:
    def user_input(self):
        self.size = int(input("Enter size of two lists:"))
        self.list_keys = []
        self.list_values = []
        for i in range(0,self.size):
            for j in range(0,2):
                element = input("Enter element [List {}]:".format(j+1))
                if j == 0:
                    self.list_keys.append(element)
                else:
                    self.list_values.append(element)
        self.dictCreation()

    def dictCreation(self):
        dict_combine = {}
        for i in range(0,self.size):
            dict_combine[self.list_keys[i]] = self.list_values[i]
        print(dict_combine)

obj = DictCreation()
obj.user_input()

