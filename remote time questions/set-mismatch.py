#leetcode
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        repeated = sum(nums)- sum(set(nums))
        missing = sum(range(1,n+1)) - sum(set(nums))
        return [repeated,missing]
