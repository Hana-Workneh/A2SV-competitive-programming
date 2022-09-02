# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:  
            return False

       
        stack = [(0,0,root)]  

        depthx = -1
        depthy = -1
        parentx = 0
        parenty = 0

        while stack:
            level, parent_val, node = stack.pop()
            if node:
                if node.val == x:
                    depthx = level
                    parentx = parent_val
                elif node.val == y:
                    depthy = level
                    parenty = parent_val
                stack.append((level+1,node.val, node.right))
                stack.append((level+1,node.val, node.left))

        return depthx != -1 and depthx == depthy and parentx != parenty