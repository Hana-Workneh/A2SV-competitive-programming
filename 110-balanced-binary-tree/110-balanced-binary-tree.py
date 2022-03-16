class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def heightCheck(node):
            if not node:
                return 0
            
            left = heightCheck(node.left)
            right = heightCheck(node.right)
            
            return 1 + max(left, right)
        
        if abs(heightCheck(root.left)-heightCheck(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)