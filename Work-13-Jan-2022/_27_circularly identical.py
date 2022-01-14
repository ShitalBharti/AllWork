#check circularly identical in two list'''


# python program to check if two
# lists are circularly identical
# using traversal

# function to check circularly identical or not
def circularly_identical(list1, list2):
    # doubling list
    list1.extend(list1)

    # traversal in twice of list1
    for i in range(len(list1)):

        # check if sliced list1 is equal to list2
        if list2 == list1[i: i + len(list2)]:
            return True
    return False


# driver code
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0,10]

# check for list 1 and list 2
if (circularly_identical(list1, list2)):
    print("Yes")
else:
    print("No")