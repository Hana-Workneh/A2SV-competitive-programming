# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.minDiff = float('inf')
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def tvs(rt):
            if rt == None:
                return
            tvs(rt.left)
            if self.pre == None:
                self.pre = rt
            else:
                self.minDiff = min(self.minDiff,rt.val - self.pre.val)
                self.pre = rt
            tvs(rt.right)
        tvs(root)
        return self.minDiff