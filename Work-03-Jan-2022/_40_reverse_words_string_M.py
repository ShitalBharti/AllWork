'''Reverse word in a string'''
def word_reverse(str1):
    words=str1.split(' ')
    rev_str=' '.join(reversed(words))
    return(rev_str)


str1="work is worship"
print("the original string is",str1)
print("the reversed string is",word_reverse(str1))