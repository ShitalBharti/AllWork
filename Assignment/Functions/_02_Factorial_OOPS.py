class Factorial:
    def user_input(self):
        self.number = input("Enter positive number:")
        if self.number.isdigit():
            self.number = int(self.number)
            fact = self.factorial(self.number)
            return fact
        else:
            print("Enter only positve integer!")
            self.user_input()

    def factorial(self,number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            res = number * self.factorial(number-1) * 1
            return res

factobj = Factorial()
output = factobj.user_input()
print("Factorial is:{}".format(output))