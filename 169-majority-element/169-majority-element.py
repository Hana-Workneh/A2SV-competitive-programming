class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = Counter(nums)
        n = len(nums)
        for i in nums.values():
            if i >= n//2 and i == max(nums.values()):
                ind= list(nums.values()).index(i)
                key = list(nums.keys())
                return key[ind]