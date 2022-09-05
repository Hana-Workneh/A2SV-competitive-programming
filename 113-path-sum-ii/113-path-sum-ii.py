# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def path(root, target, res, ans):
    
    if root is None:
        return
    if root.left is None and root.right is None:
        target = target-root.val
        if target == 0:
            res.append(root.val)
            ans.append(res)
        return
    
    path(root.left, target-root.val, res+[root.val], ans)
    path(root.right, target-root.val, res+[root.val], ans)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        path(root, targetSum, [], ans)
        
        return ans