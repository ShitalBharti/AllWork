"""
Python provides two functions: perf_counter() and process_time() of "time" module to measure the time difference between two points
in a program. Hence, these functions can be used to measure the time taken or execution of a Python program.

-> perf_counter():  It returns the time duration in fractional seconds.
                    It measures the time taken by program to execute a group of statements.
                    It includes the time elapsed during sleep of the processor.
-> process_time():  It returns the time duration in fractional seconds.
                    It measures the total time taken by the program and CPU in executing a group of statements.
                    But it will not count the time elapsed during sleep of the processor.

"""

# program to find execution time of a program

from time import *

# starting time
t1 = perf_counter()

i, sum = 0, 0
while i<1000000:
    sum+=i
    i+=1

sleep(3)

# ending time
t2 = perf_counter()

print("Execution time: = %f seconds"%(t2-t1))
