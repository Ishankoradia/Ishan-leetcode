# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        headPointer = head
        
        pointer = head
        
        c = n
        
        l = 1
        
        while(headPointer.next != None):
            
            l +=1
            
            headPointer = headPointer.next
            
            if(c == 0):
                pointer = pointer.next
            else: 
                c -= 1
         
        if(l > n):
            pointer.next = pointer.next.next
        elif(l == 1):
            head = head.next
        elif(l == n):
            pointer.val = pointer.next.val
            pointer.next = pointer.next.next
        
        return head