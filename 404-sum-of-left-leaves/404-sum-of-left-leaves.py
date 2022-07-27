# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.value = 0
        
        def dfs(node):
            if node == None:
                return
            if node.left and node.left.left == node.left.right == None:
                self.value += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        return self.value