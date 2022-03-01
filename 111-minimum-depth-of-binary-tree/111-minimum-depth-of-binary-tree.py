# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return inf
            if root.left == None and root.right == None:
                return 1
            return 1 + min(dfs(root.left), dfs(root.right))
        ans = dfs(root)
        if ans !=inf:
            return ans
        return 0