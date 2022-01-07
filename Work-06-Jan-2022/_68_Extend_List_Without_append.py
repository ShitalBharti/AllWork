# Extend a list without append

lst1 = [1,2,3]
lst2 = [4,5,6]

lst1[3:] = lst2
print(lst1)


lst1.extend(lst2)

print(lst1)