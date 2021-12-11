def mulNumbers():
    range_in = int(input("Enter Range: "))
    no_list = []
    mul = 1
    for i in range(1, range_in + 1):
        no = int(input('Enter no {}: '.format(i)))
        no_list.append(no)
        mul = mul * no
    print("List Numbers are:{}".format(no_list))
    print("Multiplication of Numbers is:{}".format(mul))

mulNumbers()