#valid anagram
def anagramCheck(str1, str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False
str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
a=anagramCheck(str1,str2)
print(a)