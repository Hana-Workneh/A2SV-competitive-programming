class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i,j in enumerate(nums):
            if target == j:
                res.append(i)
        return res
