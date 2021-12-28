"""
Q. On the eve of Diwali, Hari is decorating his house with a serial light bulb set.
The serial light bulb set has N bulbs placed sequentially on a string which is programmed to change patterns every second.
If at least one bulb in the set is on at any given instant of time, how many different patterns of light can the serial light bulb set produce?

Sample Input
1 - no of lights
2  - no of lights
Sample Output
1
3
"""
import itertools

""""
result = []
ans = 1;
n = int(input("Enter no of ligths : "))
for i in range(n):
    ans = ans * 2;
    ans = ans % 100000;
    #print(ans)
    result.append(ans-1)
print("Answer: ",result)

"""
bulb_status = [0, 1]
no = int(input("Enter no. of bulbs: "))
total_list = bulb_status * no
# print(total_list)
final = list(itertools.combinations(total_list,no))
oplist = []
for item in final:
    # print(item)
    if 1 in item:
        oplist.append(item)
# print(oplist)
opset = set(oplist)
print("Combinations are: ",opset)
print("Possibilities are: ",len(opset))
