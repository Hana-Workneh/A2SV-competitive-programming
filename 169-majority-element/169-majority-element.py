class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, size = Counter(nums), len(nums)
        for key, value in count.items():
            if value > size//2:
                return key
        return 0