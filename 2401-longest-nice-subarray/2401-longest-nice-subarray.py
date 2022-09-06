class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        r = 0
        OR = 0
        while r<len(nums):
            while OR&nums[r]!=0:   
                OR^=nums[l]
                l+=1
            OR|=nums[r]
            r+=1
            ans = max(ans,r-l)
        return ans