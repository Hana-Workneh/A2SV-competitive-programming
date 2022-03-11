# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            l =traverse(left.left,right.right)
        
            r= traverse(left.right,right.left)
            
            return l and r
        
        return traverse(root.left,root.right)