# write into file until user wish to exit
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','w')
flag = True
while flag:
    string = input("Enter text to write OR if wants to exit press @:")
    if string != '@':
        f.write(string)
    else:
        print("Okay!")
        flag = False
        f.close()

print("-----------------------------------")
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','w')
print("Enter text to write (@ at the end):")
string = ''
while string != '@':
    string = input()
    if string != '@':
        f.write(string+'\n')
    else:
        print("Okay!")
        f.close()


