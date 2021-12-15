#  unzip a list of tuples into individual lists

# 1. Using for loop
tuples_list = [('Shital', 1),('Vitthal', 2),('Rakshitha', 3),('Shubham', 4)]
print("Original List:",tuples_list)
list1 = []
list2 = []
final_list = []
for item in tuples_list:
    for i in item:
        if item.index(i) == 0:
            list1.append(i)
        else:
            list2.append(i)
final_list.append(tuple(list1))
final_list.append(tuple(list2))
print("Modified list:",final_list)

print("------------------------------------------------")

# 2. using built in functions
final_list = []
final_list =list(zip(*tuples_list))
print("Modified list:",final_list)

