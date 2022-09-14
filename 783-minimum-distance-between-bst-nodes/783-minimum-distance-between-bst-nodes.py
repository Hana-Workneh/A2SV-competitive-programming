# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans=[]
        if root is not None:
            def inorder(root,ans):
                if root.left is not None:
                    inorder(root.left,ans) 
                ans.append(root.val)
                if root.right is not None:
                    inorder(root.right,ans) 
            inorder(root,ans)
        ans.sort()
        mini=sys.maxsize
        for i in range(1,len(ans)):
            if ans[i]-ans[i-1]<mini:
                mini=ans[i]-ans[i-1]
        return mini