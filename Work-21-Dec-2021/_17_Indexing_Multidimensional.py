
# program to retrieve elements from 2d array
a = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    print(a[i])
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
print()
print("-----------------3d array------------------------")
# program to retrieve elements from 3d array
a = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k], end = '\t')
        print()
    print()

print("-----------------slicing multi-dimensional array------------------------")
b = [
    [1, 2, 3, 4, 5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]
print(b)
print(b[:3 :2])