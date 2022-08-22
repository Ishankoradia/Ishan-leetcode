# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = [] 
        while head is not None:
            l.append(head.val)
            head = head.next
        front = 0
        end = len(l)-1
        while front < end:
            if l[front] != l[end]: 
                return False
            front += 1
            end -= 1
        return True