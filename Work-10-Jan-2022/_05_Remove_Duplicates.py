def removeDuplicates(l1):
    for element in l1:
        if l1.count(element) > 1 :
            l1.remove(element)
    print(l1)
    return len(l1)

s1 = int(input("Enter sizes of list : "))
list1 = [int(input("Enter element: ")) for i in range(0, int(s1))]
k = removeDuplicates(list1)
print(k)
