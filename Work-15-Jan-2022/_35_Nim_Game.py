'''
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap,
return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

'''

class RemoveStones:
    def canWinNim(self,n):
        # always you go first
        # minimum stones can remove at once = 1 and max = 3
        if 1 <= n <= 3:
            return True
        elif n % 3 == 0 and n > 3:
            div = n / 3
            if div % 2 == 0:
                return False
            else:
                return True
        elif n % 3 == 1 or n % 3 == 2 and n > 3:
            quo = int(n // 3)
            if quo % 2 == 0:
                return True
            else:
                return False

n = int(input("Enter no. of stones: "))
rs = RemoveStones()
res= rs.canWinNim(n)
print(res)