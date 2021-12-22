class A:
    user_size=int(input("Enter the range :"))

    def parenthesis_append(self, result,open=0, close=0):
        if (close == A.user_size):
            #  When get the result of parentheses in given size
            print(result)


        if (open < A.user_size):
            #  Add open parentheses
            self.parenthesis_append(result + "(",
                                 open + 1, close)

        if (open > close):
            #  Add close parentheses
            self.parenthesis_append(result + ")",
                                 open, close + 1)


a=A()
a.parenthesis_append("")
