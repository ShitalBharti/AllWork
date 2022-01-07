# Iterate over two lists simultaneously

num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

length = min(len(num),len(color),len(value))
print(length)

for i in range(length):
    print(num[i],'\t',color[i],'\t',value[i])

