'''Prime number '''
number=int(input("enter the number"))
if number>1:
    for i in range(2,number):
        if number%i==0:
            print("not prime number",number)
            break
    else:
        print("a prime number",number)
else:
    print("enter the positive number")
'''print prime number between 1 to 100'''
lower=int(input("enter the number "))
upper=int(input("enter the number"))
for number in range (lower,upper+1):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                print("not prime number",number)
                break
        else:
            print("a prime number",number)
    else:
        print("enter a positive number")
