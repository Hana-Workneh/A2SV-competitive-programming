# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def pre(root,local):
            if root is None:
                return

            local[root.val]+=1
            if root.left is None and root.right is None:
                odd = 0
                for k in local:
                    if local[k]%2:
                        odd+=1
                if odd<2:
                    self.res+=1

            pre(root.left,local)
            pre(root.right,local)
            local[root.val]-=1

        pre(root,defaultdict(int))
        return self.res