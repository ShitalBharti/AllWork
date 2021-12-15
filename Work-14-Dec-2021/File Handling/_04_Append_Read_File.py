# writing into a file and reading file
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','a+')
string = input("Enter content to write:")
f.write(string)
# put the file pointer to the beginning of the file
f.seek(0,0)
string = f.read()
print(string)
f.close()

"""
f.seek(offset,fromwhere):
offset -> It represents how many bytes/characters to move.
fromwhere -> It represents from which position to move. 
0 (represents from beginning of file), 1 (represents from current position in file), 2 (represents from ending of file)

"""