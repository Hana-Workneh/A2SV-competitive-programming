# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)
            
        inorder(root)
     
        stack.sort()
        
        return stack[k-1]