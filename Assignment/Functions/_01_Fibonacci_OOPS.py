class Fibonacci:
    def user_input(self):
        self.term = input("Enter positive term only Integer:")
        if self.term.isdigit():
            self.term = int(self.term)
            if self.term == 0:
                self.term_0()
            elif self.term == 1:
                self.term_1()
            elif self.term > 1:
                self.term_grt()
        else:
            print("Enter only positve integer!")
            self.user_input()

    def term_0(self):
        print("Fibonacci series upto {}th term is:\n{}".format(self.term, self.term))
        self.continue_again()

    def term_1(self):
        print("Fibonacci series upto {}th term is:\n{}\n{}".format(self.term, 0,0 + 1))
        self.continue_again()

    # fibonacci logic
    def term_grt(self):
        res = 0
        a = 0
        b = 1
        count = 1
        print("Fibonacci series upto {}th term is:")
        while count <= self.term:
            print(res)
            count = count + 1
            a = b
            b = res
            res = a + b
        self.continue_again()

    def continue_again(self):
        cont = input("Want to continue Y/N:").lower()
        if cont == 'y':
            self.user_input()
        elif cont == 'n':
            print("Thank you!")
        else:
            print("Enter valid input!")
            self.continue_again()

fibo = Fibonacci()
fibo.user_input()