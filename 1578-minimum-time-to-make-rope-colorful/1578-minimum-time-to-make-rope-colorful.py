class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
        maxTime = neededTime[0]
        totalCost = sum(neededTime)
        for i in range(1, len(colors)):
            if colors[i] != colors[i-1]:
                totalCost -= maxTime
                maxTime = 0
            if neededTime[i] > maxTime:
                maxTime = neededTime[i] 
        totalCost -= maxTime
        return totalCost