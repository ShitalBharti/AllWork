import sympy

def checkPrime():
    range_in = int(input("Enter range:"))
    prime_list = []
    for i in range(1,range_in):
        if sympy.isprime(i) == True:
            prime_list.append(i)
    print("Prime Numbers:{}".format(prime_list))

checkPrime()