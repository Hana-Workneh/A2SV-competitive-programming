
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:   
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        res=[]                       
        while len(queue) > 0:
            total=0    
            n = len(queue)
            for i in range(0,len(queue)):   
                node = queue.pop(0)
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(total/n)
                
        return res

