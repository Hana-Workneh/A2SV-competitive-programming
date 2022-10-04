class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i, num in enumerate(nums):
            dp[i][i] = num
        
        for start in reversed(range(n)):
            for end in range(start+1, n):
                max_end = nums[end] - dp[start][end-1]      
                max_start = nums[start] - dp[start+1][end]  
                dp[start][end] = max(max_end,max_start)
        return dp[0][-1] >= 0