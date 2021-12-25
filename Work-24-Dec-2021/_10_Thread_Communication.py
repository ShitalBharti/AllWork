# python program where producer and consumer threads communicate with each other through a boolean type variable.

from threading import *
from time import *

class Producer:
    def __init__(self):
        self.lst  = []
        self.dataprodover = False

    def product(self):
        for i in range(1,11):
            self.lst.append(i)
            sleep(1)
            print("Item produce...")

        self.dataprodover = True

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        while self.prod.dataprodover == False:
            sleep(0.1)
            print(self.prod.lst)

p = Producer()

c = Consumer(p)

t1 = Thread(target=p.product)
t2 = Thread(target=c.consume)

t1.start()
t2.start()


