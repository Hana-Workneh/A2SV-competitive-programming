#leetcode
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        numSorted=sorted(nums)
        minArr=[]
        for i in range(0, len(numSorted), 2):
            minimum=min(numSorted[i],numSorted[i+1])
            minArr.append(minimum)
        maxSum=0
        for i in minArr:
            maxSum+=i
        return maxSum
