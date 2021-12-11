# accepts a string and calculate the number of upper case letters and lower case letters
def noUpperLowerCase():
    string = input("Enter String:")
    lower_list = []
    upper_list = []
    for char in string:
        if char.isalpha():
            if char.islower():
                lower_list.append(char)
            elif char.isupper():
                upper_list.append(char)

    print("Lower case characters are:{} and count = {}".format(lower_list,len(lower_list)))
    print("Upper case characters are:{} and count = {}".format(upper_list, len(upper_list)))

noUpperLowerCase()