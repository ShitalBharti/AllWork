"""
-> Even if we synchronize the threads, there is possibility of other problems like 'deadlock'.
e.g: Daily thousands of people book tickets in trains and cancel tickets also.

# bookticket thread
lock -1:
lock on train
lock -2:
lock on compartment

# cancelticket thread
lock - 2:
lock on compartment
lock -1:
lock on train

bookticket: thread will check in train if any compartment is available. If it is available it will book ticket.
cancelticket: thread will check which compartment the seat is cancel. Then it will enter train and make ticket available.

Here, bookticket threads locks on train and wants to enter compartment. Similarly, cancelticket thread locks on compartment and wants to enter in train.
But bookticket thread finds that lock is already acquire by compartment and compartment finds that lock is already acquire by bookticket.
both are waiting for each other to release lock. Neither of them are releasing lock.

This scenario is called as 'deadlock'
"""

# program to show deadlock on threads due to locks on objects.

from threading import *

l1 = Lock()
l2 = Lock()

def bookticket():
    l1.acquire()
    print("Bookticket lock on train..")
    print("bookticket wants to lock on compartment...")
    l2.acquire()
    print("bookticket lock on compartment")
    l2.release()
    l1.release()
    print("Booking ticket done!!")

def cancelticket():
    l2.acquire()
    print("Cancelticket lock on compartment..")
    print("cancelticket wants to lock on train...")
    l1.acquire()
    print("cancelticket lock on train")
    l1.release()
    l2.release()
    print("Cancellation ticket done!!")

t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)

t1.start()
t2.start()


