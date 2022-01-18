str = 'Hi hello'
print(str)
print(type(str))
long_string = '''
Hello,
How 
are 
you!
'''
print(long_string)

# String concatenation (Adding Strings together)
first_name = 'Andrei'
last_name = 'Neagoie'
full_name = first_name + last_name
print(full_name)
# print('String' + 5) # Error
# print(5 + 'String') # Error
#print(type(str(100)))

# Escape Sequence
weather = "It\'s \"kind of\" sunny"
print(weather)

# \t - tab
# \n - new line

# formatted Strings
name = 'shital'
print('hi ' + name)
print(f'hi {name}')  # need not to use tabs and spaces