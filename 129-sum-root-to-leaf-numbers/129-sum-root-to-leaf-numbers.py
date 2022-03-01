# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def recur(node,value):
            if not node.left and not node.right:
                self.total += int(value)
                return 
            
            if node.left:
                recur(node.left, value + str(node.left.val))
                
            if node.right:
                recur(node.right, value + str(node.right.val))
        
        recur(root,str(root.val))
        
        return self.total   
            
        
#         if not root.left and not root.right:
#             return root.val
        
#         stack = []
#         total = 0
#         visited = set()
        
#         stack.append(root)
        
#         while stack:
            
#             if stack[-1].left and stack[-1].left not in visited:
#                 stack.append(stack[-1].left)
#             elif stack[-1].right and stack[-1].right not in visited:
#                 stack.append(stack[-1].right)
#             elif stack[-1].left in visited or stack[-1].right in visited:
#                 visited.add(stack.pop())
#             else:
#                 st = ""
#                 for x in stack:
#                     st+= str(x.val)
#                 total += int(st)
#                 visited.add(stack.pop())
        
#         return total