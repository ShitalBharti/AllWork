'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

string = input("Enter string: ")

close = 0
open = 0

for char in string:
    if char == '(':
        close += 1
    else:
        open += 1

if close < open:
    length = close * 2
else:
    length = open * 2

print("Length of longest substring is: ",length)

