def mergeLists(l1,l2):
    l1.extend(l2)
    l1.sort()
    print("Merge List: ",l1)
'''
list1 = [1,2,4]
list2 = [1,3,4]
'''
s1,s2 = input("Enter sizes of list1 and list2: ").split()
list1 = [int(input("Enter element list1: ")) for i in range(0,int(s1)) ]
list2 = [int(input("Enter element list2: ")) for i in range(0,int(s2)) ]
mergeLists(list1,list2)
