# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:        
        lis, stack = [], []
        while head:
            lis.append(head.val)
            head = head.next
        nxt =[0]*(len(lis))
        for i in range(len(lis)):
            while stack and lis[stack[-1]] <  lis[i]:
                nxt[stack.pop()] = lis[i]
            stack.append(i)
        return nxt
            