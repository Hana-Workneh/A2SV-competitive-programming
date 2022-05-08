class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        res, arr = 0, 0
        for [start, end] in points:
            if res == 0 or start > arr:
                res, arr = res + 1, end
        return res