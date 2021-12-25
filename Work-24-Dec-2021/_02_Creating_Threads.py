"""
-> Python provides 'Thread' class of threading module that is useful to create Threads.
-> To create our own thread, we are supposed to create an object Thread class.
-> Ways to create Thread:
    -> Creating Thread without using a class.
    -> Creating a Thread by creating a subclass to Thread class.
    -> Creating a Thread without creating subclass.
"""
print("------------------------------Type 1-----------------------------")

# 1. Creating Thread without using a class.

from threading import *

# create a function
def display():
    print("Hello I am running!")

for i in range(5):
    t = Thread(target=display)
    t.start()

print("\n------------------------------Type 2-----------------------------")

def show(string):
    print(string)

for i in range(5):
    t = Thread(target=show, args = ('Hello',))
    t.start()


print("\n------------------------------Type 3-----------------------------")

# 2. Creating Thread by creating a sub class to Thread class.

class MyThread(Thread):
    # Override the run() method of Thread class
    def run(self):
        for i in range(1,6):
            print(i)

# create an instance of MyThread class
t1 = MyThread()

# start running the thread t1
t1.start()

# wait til the thread completes execution
t1.join()


print("\n------------------------------Type 4-----------------------------")

# 3. Create a Thread that access the instance variables of a class.

class MyThread1(Thread):

    # constructor that calls Thread class constructor
    def __init__(self,string):
        Thread.__init__(self)
        self.string = string

    # override the run() method of Thread class
    def run(self):
        print(self.string)

# create an instance of MyThread class and pass the string
t1 = MyThread1('Hello')

# start running the thread t1
t1.start()

# wait till the thread completes execution
t1.join()

print("\n------------------------------Type 4-----------------------------")

# 4. Create a Thread without creating sub class to Thread class

class MyThread2:

    def __init__(self,string):
        self.string = string

    def showValue(self,x,y):
        print(self.string)
        print("The args are: ",x,y)

t2 = MyThread2('Good Morning')
t = Thread(target=t2.showValue, args = (1,2))
t.start()
