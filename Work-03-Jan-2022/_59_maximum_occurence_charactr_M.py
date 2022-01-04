'''find the maximum occurrring character in a given string'''
def max_character(str1):
    ASCII_SIZE=256
    ctr=[0]* ASCII_SIZE
    max=-1
    ch=''
    for i in str1:
        ctr[ord(i)]+=1

    for i in str1:
        if max <ctr[ord(i)]:
            max =ctr[ord(i)]
            ch=i
            return ch

str1="India is a beautiful lcountry"
output=print(max_character(str1))

