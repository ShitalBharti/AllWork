# create a set
set1 = {1,2,1.5,'Shital','a', False, None}
print("Set: ",set1)

# Iterate over a set
print("---------------------------------")
for i in set1:
    print(i)

# Add member in a set
print("---------------------------------")
set1.add('Bharti')
print("After adding: ",set1)

# Remove an item from a set
print("---------------------------------")
set1.remove(2)
print("After removing: ",set1)

# Remove an item from a set if it is present in the set
print("---------------------------------")
el = input("Enter element: ")
if el.isdigit():
    el = int(el)
elif el == 'True':
    el = True
elif el == 'False':
    el = False
elif el == 'None':
    el = None
else:
    try:
        el = float(el)
    except ValueError:
        el = el
if el in set1:
    set1.remove(el)
print("After removing: ",set1)

# intersection of sets
print("---------------------------------")
set2 = {1,2,3,4,5,6}
set3 = {5,6,7,8,9}
print("Set2: ",set2)
print("Set3: ",set3)
print("Intersection: ",set2.intersection(set3))

# Create a union of sets
print("---------------------------------")
set2 = {1,2,3,4,5,6}
set3 = {5,6,7,8,9}
print("Set2: ",set2)
print("Set3: ",set3)
print("Union: ",set2.union(set3))

# Create set difference
print("---------------------------------")
set2 = {1,2,3,4,5,6}
set3 = {5,6,7,8,9}
print("Set2: ",set2)
print("Set3: ",set3)
print("Set Difference: ",set2.difference(set3))

# Create a symmetric difference.
print("---------------------------------")
set2 = {1,2,3,4,5,6}
set3 = {5,6,7,8,9}
print("Set2: ",set2)
print("Set3: ",set3)
print("Set Symmetric Difference: ",set2.symmetric_difference(set3))  # Opposite of intersection

# Clear a set.
print("---------------------------------")
set4 = {1,2,3,4,5}
print("Set before clearing: ",set4)
set4.clear()
print("Set after clearing: ",set4)   # -> empty set

# Find maximum and the minimum value in a set
print("---------------------------------")
set5 = {1,2,3,4,5}
print("Set5: ",set5)
print("Maximum value: ",max(set5))

# Find the length of a set
print("---------------------------------")
print("Length of set5: ",len(set5))