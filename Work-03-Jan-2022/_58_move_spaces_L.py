'''move spaces to the front of a given string'''

str1="my name is rakshitha"
chars=[char for char in str1 if char!=" "]
spaces=str1.count(' ')
new_string=" " * spaces
new_string+=" ".join(chars)
print(new_string)

