# Convert a given string to all uppercase

# using built-in function
def convert_upper(string):
    new_str = string.upper()
    return new_str

res = convert_upper(input("Enter String: "))
print(res)

# without using built-in function

def con_upper(string):
    new_str = []
    for char in string:
        if char >= 'a' and char <= 'z':
            nchar = chr(ord(char)-32)
            new_str.append(nchar)
    opstr = ''.join(new_str)
    return opstr

res = con_upper(input("Enter String: "))
print(res)
