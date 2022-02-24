# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        Max = []
        while head:
            Max.append(head.val)
            head = head.next
        leng = len(Max)
        return max(Max[i] + Max[leng-i-1] for i in range(leng//2))