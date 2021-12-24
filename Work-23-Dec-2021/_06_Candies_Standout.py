"""

Alice loves candies, so she went into a candy shop.
Now the shopkeeper sells candies in packets and all packets contain an odd number of candies (1, 3, 5, 7.....).
Alice wants exactly N candies but she also loves patterns so she decided to buy candies only if the number of candies in the packets
is consecutive and distinct (means she cannot buy the same candy packet more than once) and
the sum of all the candies in those packets is exactly N.

Alice has an infinite amount of money and the shopkeeper also has infinite amount candy packets,
so Alice wonders how many different sets of candy packets she can buy.

Find the number of different sets of candy packets that Alice can buy.

Input format

The first and the only line contains a single integer .

Output format

Print a single integer denoting the number of different sets of candy packets Alice can buy.

Sample Input
45
Sample Output
3

1. {5,7,9,11,13}

2.{13,15,17}

3.{45}
"""
import itertools

"""
zip() function use:
result = list(itertools.accumulate(odd_no))
print(result)

x = zip(odd_no,odd_no[1:length])
print(tuple(x))

x1 = zip(odd_no,odd_no[1:],odd_no[2:])
print(tuple(x1))

for item in (zip(odd_no,odd_no[1:],odd_no[2:])):
    total = list(itertools.accumulate(item))
    print(total[-1])

x1 = zip(odd_no,odd_no[1:],odd_no[2:],odd_no[3:])
print(tuple(x1))

x1 = zip(odd_no,odd_no[1:],odd_no[2:],odd_no[3:],odd_no[4:])
print(tuple(x1))
print("---------------------------------")
x = zip(odd_no,odd_no[1:length])
x1 = zip(odd_no,odd_no[1:],odd_no[2:])
x1 = zip(odd_no,odd_no[1:],odd_no[2:],odd_no[3:])
x1 = zip(odd_no,odd_no[1:],odd_no[2:],odd_no[3:],odd_no[4:])
"""
no = int(input("Total no. of candies alice wants: "))
odd_no = []
final_set = []
item = 0
for i in range(1, no+1):
    if i % 2 != 0:
        odd_no.append(i)
print("Odd Nos:",odd_no)
length = len(odd_no)
finalop = []
# to check if list contains the given no.

if no in odd_no:
    set1 = {no}
    finalop.append(set1)

# to perform addition on consecutive numbers in list
iterables = []
iterables.append(odd_no)
for i in range(1,length):
    iterables.append(odd_no[i:])
    result = zip(*iterables) # it will fetch all the values till it is appended
    print(tuple(result))
    for item in zip(*iterables):
        total = list(itertools.accumulate(item))
        print(total[-1],end=' ')
        if total[-1] == no:
            set2 = {item}
            finalop.append(set2)
    print()
print("---------------------")
print(finalop)
print(len(finalop))

























