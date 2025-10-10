# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        counter = 1
        while (current != None):
            length+=1
            current = current.next
        if (length % 2 == 0):
            middlePosition = (length / 2) + 1
        else:
            middlePosition = (length + 1) / 2
        current = head
        while (current != None):
            if (counter == middlePosition):
                return current
            counter+=1
            current = current.next
        
        
        