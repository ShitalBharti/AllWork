'''
#a python program to create Emp class and make all the members of the emp class available to another class
class Emp:
    #this is a constructor
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    #this is an instance method
    def display(self):
        print('Id=',self.id)
        print('Name=',self.name)
        print('salary=',self.salary)
#this class displays employee details
class Myclass:
    #method to receive Emp class instance
    #and display employee deatails
    @classmethod
    def mymethod(cls,e):
        #increment  salary of e by 1000
        e.salary+=1000;
        e.display()
#create Emp class
# e
e=Emp(10,'Rakshitha',15000.75)
e.display()
#call static method of Myclass and pass e
Myclass.mymethod(e)

#Program to calculate power value of a number with the help of a static method
#another example for static method
class Myclass:
    #method to calculate x to the power of n
    @staticmethod
    def mymethod(x,n):
        result=x**n
        print('{} to the power of {} is {}'.format(x,n,result))
#call the static method
Myclass.mymethod(5,3)
Myclass.mymethod(5,4)

#Python program to create dob class within person class
class Person:
    def __init__(self):
        self.name='charles'
        self.db=self.Dob()
    def dispaly(self):
        print('Names= ',self.name)
    #this is inner class
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1988
        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
#creating person class object
p=Person()
p.dispaly()
#create inner class object
x=p.db
x.display()
'''
#A python program to create another version of Dob class within person class
#inner class example
class Person:
    def __init__(self):
        self.name='Rakshitha'
    def dispaly(self):
        print('name= ',self.name)

    #this is inner class
    class Dob:
       def __init__(self):
            self.dd=4
            self.mm=8
            self.yy=1995
       def dispaly(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yy))

#creating person class object
p=Person()
p.dispaly()
#create DOB class object as sub object to person class object
x=Person().Dob()
x.dispaly()
print(x.yy)
