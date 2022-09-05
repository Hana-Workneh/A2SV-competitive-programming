# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, target):
            if not node:
                return
            elif not node.left and not node.right:
                if node.val == target:
                    path.append(node.val)
                    result.append(path)
                    return 
            else:
                return dfs(node.left, path+[node.val], target-node.val) or dfs(node.right, path+[node.val], target-node.val)

        result = []
        path = []
        dfs(root, path, targetSum)
        return result