string1=input('enter a string:')
t=input('enter a second string to compare:')
def isisomorphic(string1,t):
    if string1==None or t==None:
        return False
    elif string1=='' and t=='':
        return True
    else:
        if len(string1)!=len(t):
            return False
        dict1={}
        for i in range(0,len(string1)):
            c1=string1[i]
            c2=t[i]

            if c1 in dict1:
                if dict1[c1]!=c2:
                    return False
            else:
                if c2 in dict1.values():
                    return False
                dict1[c1]=c2
        return True
f=isisomorphic(string1,t)
print(f)



