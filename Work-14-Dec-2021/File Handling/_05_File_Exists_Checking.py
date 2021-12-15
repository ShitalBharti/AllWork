"""
OS(Operating System) module
    |
  path  (sub module)
    |
  isfile() (method)
"""
import os,sys
fname = input("Enter filename:")

# C:\\Users\\Admin\\Desktop\\hello.txt
if os.path.isfile(fname):
    f = open(fname, 'r')
    string = f.read()
    print(string)
else:
    print("{} does not exist".format(fname))
    sys.exit()
f.close()
