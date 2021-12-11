def checkEvenOdd():
    range_in = int(input("Enter range:"))
    even_list = []
    odd_list = []
    for i in range(1,range_in+1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print("Even No: {}".format(even_list))
    print("Odd No: {}".format(odd_list))
checkEvenOdd()