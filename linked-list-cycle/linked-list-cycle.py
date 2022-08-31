# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point = head
        pos = 0
        while point != None and point.next != None:
            if hasattr(point, 'pos'):
                return True     
            point.pos = pos
            point = point.next
            pos += 1
            
        return False