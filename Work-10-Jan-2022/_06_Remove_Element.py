def removeElement(l1,val):
    if val in l1:
        for element in l1:
            if element == val:
                l1.remove(element)
        removeElement(l1,val)
    else:
        print(l1)
    return len(l1)

s1 = int(input("Enter sizes of list : "))
list1 = [int(input("Enter element: ")) for i in range(0, int(s1))]
val = int(input('Enter value to remove: '))
k = removeElement(list1,val)
print(k)

# [0,1,2,2,3,0,4,2] val = 2 o/p = 5 list = [0,1,4,0,3]