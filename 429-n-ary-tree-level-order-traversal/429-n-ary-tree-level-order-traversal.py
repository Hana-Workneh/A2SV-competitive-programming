"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	def levelOrder(self, root: Optional['Node']) -> List[List[int]]:
		if root is None:
			return []

		queue = deque([root])
		levels = []

		while queue:
			levels.append([])
			for _ in range(len(queue)):
				node = queue.popleft()
				levels[-1].append(node.val)
				queue.extend(node.children)

		return levels
        