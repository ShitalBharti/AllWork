'''To count occurence of a substring in a string'''
def count(str1,str2):
    occurence=0
    if str2 in str1:
        occurence+=1

    return occurence

str1="my name is rakshitha"
str2="name"
print("the number of times"+ str(str2)+ "is",str(count(str1,str2)))