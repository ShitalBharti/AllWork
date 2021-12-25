"""
-> "Condition" class of threading module is useful to improve the seed of communication between the threads.
-> The Condition class object is called "condition variable" and is created as: cv = Condition()
-> This class contains methods which are used in thread communication.
    -> For example, the notify() method is useful to immediately inform the consumer thread that the data production is completed.
    -> notify_all() method is useful to inform all the waiting Consumer threads at once that the production is over. These methods are used by Producer.
    -> Consumer thread need not check if the data production is over or not through a boolean type variable.
    -> Consumer can simply wait till it gets the notification from notify().
    -> Consumer can wait using wait() method which terminates when Producer invokes notify() methods.

"""
from threading import *
from time import *

class Producer:
    def __init__(self):
        self.lst  = []
        self.cv = Condition()

    def produce(self):
        self.cv.acquire()

        for i in range(1,11):
            self.lst.append(i)
            sleep(1)
            print("Item produce...")

        self.cv.notify()
        self.cv.release()

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        self.prod.cv.acquire()
        self.prod.cv.wait(timeout = 0)
        self.prod.cv.release()
        print(self.prod.lst)

p = Producer()

c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()


