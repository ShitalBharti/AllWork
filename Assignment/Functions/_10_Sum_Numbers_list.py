def sumNumbersList():
    range_in = int(input("Enter Range: "))
    no_list = []
    for i in range(1,range_in+1):
        no = int(input('Enter no {}: '.format(i)))
        no_list.append(no)
    print("Sum of Numbers are:{}".format(sum(no_list)))

sumNumbersList()