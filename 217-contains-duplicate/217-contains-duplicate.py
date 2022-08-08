class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        for i in nums.values():
            if i >= 2:
                return True
        return False