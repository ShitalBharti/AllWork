string = 'Hello $ how are you %#'
print("Given string is: ",string)
str_add = input("Enter String to add: ")
index = int(input("Enter position to add: "))

lst_str = list(string)
#print(lst_str)

lst_str.insert(index,str_add)
#print(lst_str)

op_str = ''.join(lst_str)
print(op_str)

