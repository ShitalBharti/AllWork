"""
seek(offset, fromwhere) method - It is used to move the file pointer to another position.
                            - offset -> It represents how many bytes to move.
                            - fromwhere -> It represents from which position to move.
                                        -> It can have 3 values, 0,1,2
                                        -> 0 - beginning of file
                                        -> 1 - current position
                                        -> 2 - ending of file
tell() - It is used to return the current position of file pointer from beginning of file.

"""
with open('C:\\Users\\Admin\\Desktop\\hello.txt','r') as f:
    n = f.tell()
    print("tell() method:",n)
    print("------------------------------------------------")
    string = f.read()
    print(string)                   # without offset
    print("------------------------------------------------")
    f.seek(3)
    string = f.read()
    print("seek() method:->",string)                   # with offset
    print("------------------------------------------------")
    n = f.tell()
    print("tell() method:",n)
    print("------------------------------------------------")
    f.seek(100)
    string = f.read()
    print("seek() method:->", string)
