'''Given the head of a singly linked list, return true if it is a palindrome.
Input: head = [1,2,2,1]
Output: true'''

class Solution:
    def isPalindrome(self,head):
        self.head=head
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True
head=[1,2,2,1]
s=Solution
s.isPalindrome(head)