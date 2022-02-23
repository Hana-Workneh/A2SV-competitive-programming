class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end =0, len(nums) - 1
        ind1, ind2 = 1, len(nums)
        while start < end:
            if nums[start] + nums[end] == target:
                return [ind1, ind2]
            elif nums[start] + nums[end] < target:
                start += 1
                ind1 += 1
            elif nums[start] + nums[end] > target:
                end -= 1
                ind2 -= 1