# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=curr= ListNode()
        while head and head.next:
            nexthead =head.next.next
            node.next=head.next
            head.next.next=head
            node=head
            head=nexthead
        node.next=head
        return curr.next
