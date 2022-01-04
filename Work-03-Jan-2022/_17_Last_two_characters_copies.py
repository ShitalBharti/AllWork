def insert_end(string):
	newstr = string.strip()		# to remove white spaces from front and end
	sub_str = newstr[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))

