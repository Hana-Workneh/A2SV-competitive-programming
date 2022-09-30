from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = []
        for start, end, height in buildings:
            heights.append([start, -height])
            heights.append([end, height])
        heights = sorted(heights)
        b, ans = SortedList([0]), []
        for x, h in heights:
            if h > 0:
                b.remove(h)
            else:
                b.add(-h)
            if not ans or ans[-1][1] != b[-1]:
                ans.append([x, b[-1]])            
        return ans