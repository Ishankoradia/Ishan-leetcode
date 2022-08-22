# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:       
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        self.frontPointer = head
        
        def recursivelyCheck(currentNode=head):
            if currentNode is not None:
                if not recursivelyCheck(currentNode.next):
                    return False
                if currentNode.val != self.frontPointer.val:
                    return False
                self.frontPointer = self.frontPointer.next
            return True
        
        return recursivelyCheck()
                