class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  
        levels = []
        queue = [(root, 0)]
        while queue:
            top = queue.pop(0)
            
            topRoot = top[0]
            topRootLevel = top[1]
            
            if len(levels) < topRootLevel + 1:
                levels.append([])

            levels[topRootLevel].append(topRoot.val)
            
            child = []
            if topRoot.left:
                queue.append((topRoot.left, topRootLevel+1))
            if topRoot.right:
                queue.append((topRoot.right, topRootLevel+1))
                
        return levels