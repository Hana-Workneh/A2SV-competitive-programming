# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self,root,targetSum):
            
        if root == None:
            return False
        targetSum -= root.val
        if root.right == None and root.left == None:
            return targetSum == 0
        return self.checkTree(root.left,targetSum) or self.checkTree(root.right,targetSum)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkTree(root,targetSum)
   
            