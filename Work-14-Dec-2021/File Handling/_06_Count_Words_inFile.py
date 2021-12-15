# Counting number of lines, words and characters in a file
import os,sys
fname = input("Enter filename:")

# C:\\Users\\Admin\\Desktop\\hello.txt
if os.path.isfile(fname):
    f = open(fname, 'r')
    #string = f.read()
    #print(string)
    string2 = f.readlines()
    print(string2)
    cl = cw = cc = 0
    for item in string2:
        cl += 1
        words = item.split()
        cw += len(words)
        for char in words:
            cc += len(char)
    print("Lines Count:",cl)
    print("Word Count:", cw)
    print("Character count:", cc)
else:
    print("{} does not exist".format(fname))
    sys.exit()
f.close()


