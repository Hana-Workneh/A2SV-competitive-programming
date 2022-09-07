# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.chars = []
        self.travel(root)
        return ''.join(self.chars)
                
        
    def travel(self, root):
        if (root is None): return 
        self.chars.append(str(root.val))
        
        if (root.left is None and root.right is None): return
        
        self.chars.append('(')
        self.travel(root.left)
        self.chars.append(')')
        
        if (root.right): 
            self.chars.append('(')
            self.travel(root.right)
            self.chars.append(')')