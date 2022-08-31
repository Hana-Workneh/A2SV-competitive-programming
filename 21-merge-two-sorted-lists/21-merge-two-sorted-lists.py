# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ret = ListNode(0)
        temp = ret
        
        while list1 or list2:
            if list1 and not list2:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            elif list2 and not list1:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
            elif list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
            
        return ret.next
        