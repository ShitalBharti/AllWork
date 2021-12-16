# binary files can handle data in form of butes -> can be used to read and write text, image, audio, video files.

f1 = open("C:\\Users\\Admin\\Desktop\\teddy.jpg",'rb')   # -> rb - it will read binary file
f2 = open("C:\\Users\\Admin\\Desktop\\teddycopy.jpg",'wb')  # -> wb-it will write binary file into another file and it wil create new
                                                            # file if file is not present in system
bytes = f1.read() # -> Reading image file as bytes
# print(bytes)
f2.write(bytes) # -> Writing image file in bytes to antoher file
f1.close()
f2.close()