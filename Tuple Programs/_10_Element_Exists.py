# check whether an element exists within a tuple

tuple_1 = (1,2,2,3,3,4,5,6,6,'Shital','Shital')
print("Original tuple:",tuple_1)
element = input("Enter element:")
if element.isdigit():
    element = int(element)
elif element.isalpha():
    element = element.capitalize()
for item in tuple_1:
    if element in tuple_1:
        print("It exists")
        break
    else:
        print("Not exists")
        break
