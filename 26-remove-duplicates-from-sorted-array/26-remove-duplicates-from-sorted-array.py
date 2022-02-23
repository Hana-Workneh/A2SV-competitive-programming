class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = left = 0
        right = 1
        while(right<len(nums)):
            if nums[right]!=nums[left]:
                ind+=1
                nums[ind]=nums[right]
                left = right
            right+=1
        return ind+1