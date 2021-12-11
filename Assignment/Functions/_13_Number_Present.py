# check whether a number is in a given range
def checkNoPresent():
    list_present = [1,2,3,4,5,6,7,8,9,10]
    print("Given List:",list_present)
    no = int(input("Enter number:"))
    if no in list_present:
        print("present")
    else:
        print("not present")
checkNoPresent()