#leetcode
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = list(set(nums))
        n.sort()
        k = len(n) 
        for i in range(k):
             nums[i]=n[i]
        return k
