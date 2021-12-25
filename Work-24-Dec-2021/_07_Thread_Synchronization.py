"""
Definition: When a thread is acting on an object, preventing any other thread to act on same object is called 'Thread Synchronization' or 'Thread Safe'.
-> Object on which threads are synchronized is called "synchronized object" or "mutex"(mutually exclusive lock).
-> Thread Synchronization is done using following technique:
    -> Using locks
    -> Using semaphores

1. Locks:
-> It can be use to lock the object on which the thread is acting.
-> When thread enters the object, it will lock the object and after the execution is completed, it will unlock the object and comes out of it.

2. Semaphore:
-> A semaphore is an object that provides synchronization based on a counter. A semaphore is created as an object of semaphore class.
"""

# program to achieve thread synchronization using locks
import threading
from threading import *
from time import *

class Railway:
    def __init__(self,available):
        self.available = available
        self.l = Lock()

    def reserve(self, wanted):
        self.l.acquire()
        print("Available no. of berths: ",self.available)

        if self.available >= wanted:
            name = threading.currentThread().getName()
            print("{} berth is alloted for {}".format(wanted,name))
            # time to print ticket
            sleep(1.5)
            self.available -= wanted

        else:
            print("sorry, no berths")
        self.l.release()

ticket = Railway(1)

t1 = Thread(target=ticket.reserve, args=(1,))
t2 = Thread(target=ticket.reserve, args=(1,))

t1.setName('First Person')
t2.setName('Second Person')

t1.start()
t2.start()