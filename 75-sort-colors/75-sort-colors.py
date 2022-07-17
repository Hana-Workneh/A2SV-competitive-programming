class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red, white, blue = 0, 0, 0
        
        for i in range(n):
            if nums[i] == 0:
                red += 1
            if nums[i] == 1:
                white += 1
            if nums[i] == 2:
                blue += 1
    
        for i in range(red):
            nums[i] = 0
        for i in range(white):
            nums[red + i]=1
        for i in range(blue):
            nums[white + red + i]=2
 