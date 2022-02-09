
try:
    numlst = [int(x) for x in input("Enter elements: ").split(",")]
    target = int(input("Enter target:   "))
except:
    numlst  = []
    target = 0
finally:
    print(numlst)

    strdig = ''
    for element in numlst:
        strdig = strdig + str(element)

    ansl = strdig.find(str(target))
    ansr = strdig.rfind(str(target))

    ans = [ansl,ansr]
    print(ans)
