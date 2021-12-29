# declaring a string variable
string = input("Enter a string: ")

# index to remove character at
n = int(input("Enter index to remove character at: "))

# declaring an empty string variable for storing modified string
modified_str = ''

# iterating over the string
for char in range(0, len(string)):

    # checking if the char index is equivalent to n
    if (char != n):
        # append original string character
        modified_str += string[char]

print("Modified string after removing ", n, "th character ")
print(modified_str)