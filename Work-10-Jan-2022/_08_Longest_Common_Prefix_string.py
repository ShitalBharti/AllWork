
def longestPrefix(l):
    print(l)
    finlst = []
    for element in l:
        oplst = []
        for i in range(len(element)):
            temp = element[:i+1]
            oplst.append(temp)
        finlst.append(oplst)
    print(finlst)

    size = len(finlst)
    #print(size)

    for i in range(size-1):
        temp = set(finlst[i]).intersection(set(finlst[i+1]))
        #print(temp)

    if len(temp) == 0:
        return ''
    else:
        maxprefix = max(temp)
        print(maxprefix)


s1 = int(input("Enter sizes of list : "))
list1 = [input("Enter element: ") for i in range(0, int(s1))]
longestPrefix(list1)
