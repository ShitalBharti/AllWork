"""
Q. player A and B playing a game, both players have given same string and both players have to make substring using letters of string.
B has to make words starting with consonants, A has to make words starting with vowels.Count total no of substrings, if count of any player is greater then annouce it as winner.
e.g Shital Bharti
A - ital Bharti - 1, al Bharti - 1, i - 2, ital - 1, it - 1, arti - 1, ar - 1, al - 1 total = 9
B -
Consonants - B,C,D,F,G,J,K,L,M,N,P,Q,S,T,V,X,Z,H,R,W,Y.
"""
import itertools
string = 'hello'.lower()
length = len(string)
result = []
oplist = []
A_dict = {}
B_dict = {}
for i in range(1,length+1):
    result.append(list(itertools.combinations(string, i)))
for item in result:
    # print(item)
    for element in item:
        str1 = ''.join(element)
        oplist.append(str1)
#print(oplist)
# for item in oplist:
#     print(item)
for string2 in oplist:
    if string2[0] in ['a','e','i','o','u']:
        A_dict[string2] = A_dict.get(string2,0)+1
    else:
        B_dict[string2] = B_dict.get(string2, 0) + 1

print(A_dict)
print(B_dict)
if sum(A_dict.values()) > sum(B_dict.values()):
    print("A is winner - Length ",sum(A_dict.values()))
else:
    print("B is winner - Length ", sum(B_dict.values()))


# string2[0] in ['b','c','d''f','g','j','k','l','m','n','p','q','s','t','v','x','z','h','r','w','y']:
