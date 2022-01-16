num = [2,3,7,4,5,6,10,11,120]

#2
largest_num = num[0]
second_largest_num = num[0]
third_largest_num = num[0]

#3
for i in num :
    #4
    if i > largest_num :
        third_largest_num = second_largest_num
        second_largest_num = largest_num
        largest_num = i
    #5
    elif i > second_largest_num :
        third_largest_num = second_largest_num
        second_largest_num = i
    #6
    elif i > third_largest_num :
        third_largest_num = i

#7
print("Third largest number of the list is {}".format(third_largest_num))