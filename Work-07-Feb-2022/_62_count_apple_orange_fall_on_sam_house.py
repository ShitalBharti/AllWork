'''

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:

The red region denotes the house, where  is the start point, and  is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
Assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. *A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right. *


'''
def count_sams_got_apple_orange(s, t, a, b, apples, oranges):
    apple_collected_list=[a+x for x in apples]
    orange_collected_list=[b+x for x in oranges]
    apples_count=0
    orange_count=0
    for x in apple_collected_list:
        if x in range(s,t+1):
            apples_count+=1
    for x in orange_collected_list:
        if x in range(s,t+1):
            orange_count+=1
    print(apples_count)
    print(orange_count)

count_sams_got_apple_orange(7,10,4,12,[2,3,-4],[3,-2,-4])
