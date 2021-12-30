def towers(n,a,b):
    if n==1:
        b.extend(a)
    else:
        towers(n-1,a,b)
    #print("List b=",b)
    return b

n = int(input("Enter no. of disks.."))
a = []
for i in range(1,n+1):
    a.append(i)
    #print(i)
print("List a=",a)
b = []
res = towers(n,a,b)
print("List b=",res)