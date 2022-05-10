class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = nums[0]
        res = max(left, nums[1])
        
        for i in range(2, len(nums)):
            left, res = res, max(res, left+nums[i])
        
        return res