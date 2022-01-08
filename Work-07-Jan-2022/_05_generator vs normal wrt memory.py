#Generator vs Normal collections wrt Memory utilization.

list1=[x*x for x in range(10)]
print(list1)

#Normal collection
#list1=[x*x for x in range(10000000000000000)]
#print(list1[0])
#will get memory error because all these values are required
#to store in the memory

#generators
g=(x*x for x in range(100))
print('using generators',next(g))
#we wont get any memory error because the values wont be stored at the beginning.