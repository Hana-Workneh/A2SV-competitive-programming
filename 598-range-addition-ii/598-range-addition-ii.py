class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        for i, j in ops:
            m, n = min(m, i), min(n, j)
        return m * n