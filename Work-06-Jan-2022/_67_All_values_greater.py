# Find all the values in a list are greater than a specified numberFind all the values in a list are greater than a specified number

lst1 = [10,11,13,9]
no = int(input("Enter no: "))
length = len(lst1)
count = 0

for element in lst1:
    if element > no:
        count += 1

if count == length:
    print("All values are greater!")
else:
    print("All values are not greater!")
