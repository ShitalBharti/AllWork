# python program that performs two tasks using two threads simultaneously.
from threading import *
from time import *

class Theatre:

    def __init__(self, string):
        self.string = string

    def movieshow(self):
        for i in range(1,6):
            print(self.string,":",i)
            sleep(0.1)

theatre1 = Theatre('Cut Ticket')
theatre2 = Theatre('Show chair')

t1 = Thread(target=theatre1.movieshow())
t2 = Thread(target=theatre2.movieshow())

t1.start()
t2.start()

"""
Conclusion: o/p of this program may vary if we run several times. Some show chairs are running before ticket cut. This pehnomenon is called as 'race condition'.
Definition: Race condition is a situation that occurs when threads are not acting in an expected sequence, thus leading to unreliable output. 
            Race condition can be eliminated using 'thread synchronization'.
"""