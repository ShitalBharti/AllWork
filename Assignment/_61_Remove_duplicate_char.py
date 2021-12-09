# remove duplicate characters of a given string

string = input("Enter string:")
str_list = []
for i in string:
    str_list.append(i)
str_set = set(str_list)
print(str_set)
opstring = ''
for i in str_set:
    opstring = opstring + i
print(opstring)
