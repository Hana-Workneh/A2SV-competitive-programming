# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        def get_count(node,path_max,count):
            if node == None:
                return count
            if path_max <= node.val : 
                count += 1
    
            count = get_count(node.left,max(path_max,node.val),count)
            count = get_count(node.right,max(path_max,node.val),count)
            
            return count
        return get_count(root,root.val,0)
        