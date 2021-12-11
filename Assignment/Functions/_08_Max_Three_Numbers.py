def checkMax():
    list_no = []
    for i in range(1,4):
        number = int(input("Enter Number {}:".format(i)))
        list_no.append(number)
    print("Maximum Number is {}:".format(max(list_no)))

checkMax()