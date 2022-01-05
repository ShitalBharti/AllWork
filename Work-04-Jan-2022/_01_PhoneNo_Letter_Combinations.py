'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

'''
import itertools

# dict1 = {'2':['a','b','c'],'3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
dict1 = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

print("Letters associated with digits are: ")
print(dict1)

oplist = []; flag = False

digits = input("Enter digits: <=4 and >= 0 ")

if 0 <= len(digits) <= 4:
    for char in digits:
        if char in dict1.keys():
            flag = True
        else:
            print('Digits exceeds 2-9')
            flag = False
            break
    if flag == True:
        for char in digits:
            oplist.append(dict1.get(char))
        res = list(itertools.product(*oplist))
        # print("Combinations ",res)
        fin_list = []
        for el in res:
            ch = ''.join(el)
            fin_list.append(ch)
        print("After joining ",fin_list)
else:
    print('Digits length exceeds 0-4')