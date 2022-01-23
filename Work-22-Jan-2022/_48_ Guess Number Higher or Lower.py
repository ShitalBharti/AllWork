#374. Guess Number Higher or Lower
#if the number you have entered is greather than the number num>pick
#if the number you have entered is less than the number num<pick
#else this is the number
import random
import os
def clearconsole():
    command='clear'
num=random.randint(1,100)

while True:
    pick=int(input("enter the number"))
    if num>pick:
        print("num>pick")
    elif num<pick:
        print("num<pick")
    else:
        print("this is the number ",num)