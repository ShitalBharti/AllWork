'''Rotate string
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.'''
#shifting to one place
#string1=(input('enter a string:'))
#print(string1[1:] + string1[:1])
#d=length like how many element rotates
'''seperate the string in two parts... first and second
for left rotation lfirst=str[0:d] and lsecond=str[d:]
for right rotation rfirst=str[0:len(str)-d] and rsecond=
str[len(str)-d:]
'''
def rotate(s,g):
    temps = ''
    length = len(s)
    i = 0
    while i < length:
        startindex = s[0]
        temps = s[1:]
        temps = temps + startindex
        s = temps
        print(temps)
        if temps == goal:
            return True
        i += 1
    if temps != goal:
        return False

string = input("Enter String: ")
goal = input("Enter Goal: ")
res = rotate(string,goal)
print(res)



