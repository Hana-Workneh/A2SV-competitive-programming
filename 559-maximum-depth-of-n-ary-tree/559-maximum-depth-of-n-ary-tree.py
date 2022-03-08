"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(Node): 
            if not Node:
                return 0
            res=[0]
            for child in Node.children:
                res.append(dfs(child)) 
            return max(res)+1
        
        return dfs(root)