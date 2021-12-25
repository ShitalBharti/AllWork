from threading import *
from time import *

class MyThread:

    # method that perform three tasks one by one
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("boil milk and tea powder for 5 minutes")
        sleep(5)
        print('Done')

    def task2(self):
        print("add sugar and boil for 3 minutes")
        sleep(3)
        print('Done')

    def task3(self):
        print("filter it and serve")
        print('Done')

tea = MyThread()

t = Thread(target=tea.prepareTea)
t.start()




