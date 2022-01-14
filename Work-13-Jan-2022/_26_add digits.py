#given an integer num,repeatedly add all its digits until
#the result has one digit,and return it

def addinteger(num,add = 0):
    if 0 <= num < 10:
        print(num)
    else:
        while num != 0:
            rem = num % 10
            add = add + rem
            num = int(num / 10)
        num = add
        #print(num)
        addinteger(num,add = 0)

num=int(input('enter a number:'))
addinteger(num)



