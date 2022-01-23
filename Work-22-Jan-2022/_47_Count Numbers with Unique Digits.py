#357. Count Numbers with Unique Digits
#count the numbers of unique digits in a given range



count=0
lst=[str(ele)  for ele in range(1000000)]
n=int(input("enter how many digits"))
for i in lst:
    if len(i)==n:
        rev=i[::-1]
        if n>1:
            if rev!=i:
                print(i,end=" ")
                count+=1
        else:
            print(i, end=" ")
            count += 1


print("\n","the total count is",count)
