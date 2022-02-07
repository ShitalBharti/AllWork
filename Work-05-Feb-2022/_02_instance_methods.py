# A class to handle dposits and withdrawls in a bank
import sys
class Bank(object):
    """Bank related transactions"""
    #to initialize  name and balance instance vars
    def __init__(self,name,baalnce=0.0):
        self.name=name
        self.balance=baalnce

    #to add deposit amount to balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    #to deduct withdrawal amount from balance
    def withdaaw(self,amount):
        if amount>self.balance:
            print('balance amount is less so no withdrawl.')
        else:
            self.balance-=amount
        return self.balance
    #using the bank class
    #create an account with the given name and baalnce 0.00
    name=input('Enter name: ')
    b = Bank(name)

    while(True):
        print('d -Deposit,W -Withdraw,e-Exit')
        choice=input('your choice:')
        if choice=='e' or choice=='E':
            sys.exit()
        #amount for deposit or withdraw
        amt=float(input('Enter amount: '))

        #do the transaction
        if choice=='d' or choice=='D':
            print('Baalnce after deposit: ',b.deposit(amt))
        elif choice=='w' or choice == 'W':
            print('balance after withdrawal: ',b.withdraw(amt))
