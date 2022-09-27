class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if nums[0] == 0:
            sums = {0: 2}
        else:
            sums = {nums[0] : 1, -1 * nums[0] : 1}
            
        for i in range(1, len(nums)):
            num = nums[i]
            new_sums = {}
            for k, v in sums.items():
                if (k + num) not in new_sums:
                    new_sums[k + num] = sums[k]
                else:
                    new_sums[k + num] += sums[k]
                    
                if (k - num) not in new_sums:
                    new_sums[k - num] = sums[k]
                else:
                    new_sums[k - num] += sums[k]
            
            sums= new_sums
            
        return sums[target] if target in sums else 0