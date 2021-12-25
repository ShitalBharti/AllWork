import threading
from threading import *
from time import *

class Railway:
    def __init__(self,available):
        self.available = available

    def reserve(self, wanted):
        print("Available no. of berths: ",self.available)

        if self.available >= wanted:
            name = threading.currentThread().getName()
            print("{} berth is alloted for {} ".format(wanted,name))
            # time to print ticket
            sleep(1.5)
            self.available -= wanted

        else:
            print("sorry, no berths")

ticket = Railway(1)

t1 = Thread(target=ticket.reserve, args=(1,))
t2 = Thread(target=ticket.reserve, args=(1,))

t1.setName('First Person')
t2.setName('Second Person')

t1.start()
t2.start()