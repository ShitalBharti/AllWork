# takes a list and returns a new list with unique elements of the first list.

def uniqueElements():
    range_in = int(input("Enter Range: "))
    no_list = []
    for i in range(1, range_in + 1):
        element = input('Enter element {}: '.format(i))
        no_list.append(element)
    print("Original List:{}".format(no_list))
    opset = set(no_list)
    oplist = list(opset)
    print("Unique List:{}".format(oplist))

uniqueElements()