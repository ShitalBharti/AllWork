"""
-> Thread represents a separate path of execution of a group of statements.
-> In a python program, if we write a group of statements, then these statements are executed by PVM(Python Virtual Machine) one by one.
-> This execution is called as Threads.
"""

# 1. Program to find currently running thread in a python program.

import threading

print("Let us find current thread: ")

# find name of present thread
print("Currently running thread: ",threading.currentThread().getName())

# check if it is main thread or not
if threading.currentThread() == threading.main_thread():
    print("Main thread")
else:
    print("Not main thread")


"""
* Single Tasking -> Only one task is given to the processor at a time.
* Multi Tasking -> Several task are given to processor at a time.
    -> Time Slice: Time duration given to each task by processor.
    -> Round Robin: e.g 4 tasks are allocated to processor. Time for each task is 1/4 milliseconds. 
                    -> Task1: processor spends 1/4 ms on this task. Still task is not completed it will move to second task after completion of 1/4 ms.
                    -> Task2: processor spends 1/4 ms on this task. Still task is not completed it will move to Third task after completion of 1/4 ms.
                    -> Task3: processor spends 1/4 ms on this task. Still task is not completed it will move to Fourth task after completion of 1/4 ms.
                    -> Task4: processor spends 1/4 ms on this task. Still task is not completed it will move to First task after completion of 1/4 ms.
                    -> Tasks will complete in "circular manner" spending given time on each task.
    -> This technique will give the feel that processor is executing all jobs simultaneously.
    -> Hence, this is called as "multi-tasking."
    -> Main advantage of multitasking is to use processor time in a better way. We are engaing processor time and it is not sitting idle. It helps us to achieve good performance.
    -> Multi-Tasking is of two types:
                    -> a) Process-based b) Thread-based
                    -> In process based several programs are executed at a time.
                    -> In thread based several parts of same program is executed at a time.
    -> Uses of Threads:
                    -> Threads are highly useful when we want to perform more than task simultaneously. This is called as "concurrent programming".
                    -> Threads are mainly used in server-side programs to serve the needs of multiple clients on a network or Internet.
                    -> Threads are also used to create games and animation. 
 """