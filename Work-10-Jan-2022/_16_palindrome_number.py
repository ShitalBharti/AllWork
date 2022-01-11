'''Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the
 same backward as forward. For example, 121 is a palindrome while 123 is not.'''

def ispalindrome(str):
    for i in range(0,len(str)//2):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
x="1211"
if(ispalindrome(x)==True):
    print("it is a palindrome")
else:
    print("it is not palindrome")
