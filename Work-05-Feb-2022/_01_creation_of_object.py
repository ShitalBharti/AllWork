'''
#instance variable and instance method
class Student:
    #this is a special method called constructor
    def __init__(self):
        self.name='Rakshitha'
        self.age='26'
        self.marks=900
    #this is an instance method
    def talk(self):
        print('hi,i am ' ,self.name)
        print('my age is ',self.age)
        print('my marks are',self.marks)

#create an instance to Stuent class
s1=Student()

#call the method using the instance
s1.talk()

#A python program to create Student class with a constructor having more than one parameter
class Student:
    #this is constructor
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m
    #this is an instance method
    def display(self):
        print('hi',self.name)
        print('your marks',self.marks)
#constructor is called without any arguments
s=Student()
s.display()
print('----------------')
s1=Student('rakshitha',4588)
s1.display()
print('-------------')

#A python program to unserstand instance variables
#instance vars example
class Sample:
    #this is a constructor
    def __init__(self):
        self.x=10
    #this is an instance method
    def modify(self):
        self.x+=1
#create 2 instances
s1=Sample()
s2=Sample()
print('x in s1= ',s1.x)
print('x in s2= ',s2.x)
#modify x in s1
s1.modify()
print('x in s1= ',s1.x)
print('x in s2=',s2.x)

#class variables and static variables
class sample:
    #this is a class var
    x=10
    #this is a class method
    @classmethod
    def modify(cls):
        cls.x+=1

#create 2 instances
s1=sample()
s2=sample()
print(' x in s1= ',s1.x)
print('x in s2=',s2.x)
#modify x in s1
s1.modify()
print(' x in s1= ',s1.x)
print('x in s2= ',s2.x)

#python program using a student class with instance method to process the data of several students
#instance methods to process data of the objects
class Student:
    #this is a constructor
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m
    #this is an instance method
    def display(self):
        print('hi',self.name)
        print('your marks',self.marks)
    #to calculate grades based on marks
    def calculate(self):
        if(self.marks>=600):
            print('you got first grade')
        elif(self.marks>=500):
            print('you got second grade')
        elif(self.marks>=350):
            print('you got third grade')
        else:
            print('you are failed')

#create instances with some data from keyboard
n=int(input('How many students? '))
i=0
while (i<n):
    name=input('enter name: ')
    marks=int(input('enter marks: '))
    s=Student(name,marks)
    s.display()
    s.calculate()
    i+=1
    print('---------------------------')

#python program to store data into instances using mutator method and to retrieve data from the instances using accessor methods
#accessor and mutator methods
class Student:
    #mutator method
    def setName(self,name):
        self.name=name
    #accessor method
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks


#create instances with some data rom keyboard

n=int(input('how many students? '))
i=0
while(i<n):
    #create Student class instance
    s=Student()
    name =input('enter name: ')
    s.setName(name)
    marks=int(input('enter marks: '))
    s.setMarks(marks)

    #retrieve data from student class instance
    print('hi',s.getName())
    print('your marks',s.getMarks())
    i+=1
    print('--------')

#python programe to use class method to handle the common feature of all the instances of bird classes
#understanding class methods
class Bird:
    #this is a class var
    wings=2
    #this is class method
    @classmethod
    def fly(cls,name):
        print('{} files with {} wings'.format(name,cls.wings))
#dispaly inforamtion for 2 birds
Bird.fly('sparrow')
Bird.fly('pigeon')
#A python program to create a static method that counts the number of instances created for a class
#understanding static methods
class Myclass:
    #this is a class var or static var
    n=0
    #constructor that increments n when an instance is created
    def __init__(self):
        Myclass.n=Myclass.n+1
    #this is a static method to display the no. of instances
    @staticmethod
    def noobjects():
        print('no. of instances created:',Myclass.n)
#create 3 instances
obj1=Myclass()
obj2=Myclass()
obj3=Myclass()
obj4=Myclass()
Myclass.noobjects()

#a pyhton program to create a ststic method that calculates the square root value of a given number
#a static method to find square root value
import math
class Sample:
    @staticmethod
    def calculate(x):
        result=math.sqrt(x)
        return result
#accept a number fromthe keyvboard
num=float(input('enter a number: '))
#call the static method and pass num
res=Sample.calculate(num)
print('the square root of {} is{:.2f}'.format(num,res))
'''




