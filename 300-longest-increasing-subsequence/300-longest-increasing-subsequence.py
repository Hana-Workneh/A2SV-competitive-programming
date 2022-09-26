class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    temp = arr[i]+1
                    if temp > arr[j]:
                        arr[j] = temp
        return max(arr) 