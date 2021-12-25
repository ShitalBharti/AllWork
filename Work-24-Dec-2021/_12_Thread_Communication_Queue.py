"""
Queue class of queue module is useful to create a queue that holds the data produced by the Producer.
The data can be taken from the queue and utilized by the consumer.
A queue is a FIFO(First in First out) structure where the data is stored from one side and deleted from other side.
Queues are useful when several producers wants to communicate with several consumers. Another advantage is that while using queues, we need not use locks since queues are thread safe.
"""

from threading import *
from time import *
from queue import *

class Producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(1,11):
            print("Producing item...")
            self.q.put(i)
            sleep(1)

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        for i in range(1, 11):
            print("Receiving item...:", self.prod.q.get(i))

p = Producer()

c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
