# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        next1 = None
        while current != None:
            next1 = current.next
            current.next = prev
            prev = current
            current =  next1
            
        return prev
            