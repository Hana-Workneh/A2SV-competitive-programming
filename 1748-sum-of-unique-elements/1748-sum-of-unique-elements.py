class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        Sum=0
        for i in nums:
            if count[i]==1:
                Sum+=i
        return Sum