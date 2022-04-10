class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, res = prices[0], 0
        for num in prices:
            res = max(res, num-minimum)
            minimum = min(minimum, num)  
            
        return res