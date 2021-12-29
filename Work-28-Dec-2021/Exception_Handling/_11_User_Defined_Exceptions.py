"""
In some situations where none of the exception in Python are useful for the programmer. In that case, the programmer has to create his own exception and raise it.
"""

# program to create our own exception and raise it when needed.
class MyException(Exception):
    def __init__(self,arg):
        self.msg = arg

def check(dict):
    for k,v in dict.items():
        print('Name = {} Balance = {:.2f}'.format(k,v))
        if v<2000.00:
            raise MyException('Balance amount is less in the account of '+k)

bank = {'a':5000.00, 'b':8800.50, 'c':1990.00, 'd':3000.00}
try:
    check(bank)
except MyException as me:
    print(me)