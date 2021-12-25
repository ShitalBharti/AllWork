"""
-> Sometimes, we need threads to run continously in memory.
    -> e.g Internet Server or garbage collector.
-> Such threads which run continously are called "daemon" threads.
-> Generally, daemon threads are use to perform some background tasks.
"""
# program to understand creation of daemon thread.

from threading import *
from time import *

def display():
    for i in range(5):
        print("Normal thread")
        print(i+1)
        sleep(1)

def display_time():
    while True:
        print("Daemon thread")
        print(ctime())
        sleep(2)

t = Thread(target=display)
t.start()

d = Thread(target=display_time)
d.daemon = True
d.start()
# d.join()  # due to this statment PVM waits to complete execution of daemon thread, without this statement, daemon thread will execute only till display() method executes.