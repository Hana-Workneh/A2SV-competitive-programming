# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def dfs(root, val, parent=None, level=0):
            if not root:
                return
            
            if root.val==val:
                return (parent, level)
            
            return dfs(root.left, val, root, level+1) or dfs(root.right, val, root, level+1)
        x_parent, x_level=dfs(root, x)
        y_parent, y_level=dfs(root, y)
        
        return x_level==y_level and x_parent !=y_parent