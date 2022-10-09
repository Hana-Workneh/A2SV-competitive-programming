# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        our_set=set()
        def dfs(node) :
            if not node :
                return False
            t = k - node.val
            if t in our_set :
                return True
            else:
                our_set.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
