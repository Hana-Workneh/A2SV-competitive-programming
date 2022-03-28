class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i == j:
                    Min = nums[i]
                    Max = nums[i]
                else:
                    Max = max(Max, nums[j])
                    Min = min(Min, nums[j])
                    total += (Max - Min)
            
        return total