from zipfile import *

f = ZipFile('C:\\Users\\Admin\\Desktop\\test.zip', 'w', ZIP_DEFLATED)
f.write('C:\\Users\\Admin\\Desktop\\teddy.jpg')
f.write('C:\\Users\\Admin\\Desktop\\hello.txt')
print("Zip file created...")
f.close()