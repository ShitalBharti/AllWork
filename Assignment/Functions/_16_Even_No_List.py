# print the even numbers from a given list

def printPrime():
    range_no = int(input("Enter range:"))
    no_list = []
    even_no = []
    for i in range(0,range_no+1):
        no = int(input("Enter number:"))
        no_list.append(no)
        if no % 2 == 0:
            even_no.append(no)
    print("Original List: {}".format(no_list))
    print("Even No List: {}".format(even_no))
printPrime()




