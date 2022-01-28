# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 
        first = head
        while (head):
            n += 1
            head=head.next
        i = n//2
        while first:
            if i == 0:
                return first
            i-=1
            first=first.next
           
            
