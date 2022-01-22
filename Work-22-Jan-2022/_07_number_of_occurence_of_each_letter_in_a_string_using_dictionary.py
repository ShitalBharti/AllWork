#finding how many times each letter is repeated in a string
str="Book"
dict1={}
for i in str:
    dict1[i]=dict1.get(i,0)+1
for k,v in dict1.items():
    print('{}:{}'.format(k,v))