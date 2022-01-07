# Find the list in a list of lists whose sum of elements is the highest

lst1 = [[1,2,3],[4,5,6],[7,8,9]]
oplst = {}

for element in lst1:
    total = sum(element)
    oplst[total] = element

print(oplst)
maxvalue = max(oplst.keys())
lst2 = oplst.get(maxvalue)
print(lst2)