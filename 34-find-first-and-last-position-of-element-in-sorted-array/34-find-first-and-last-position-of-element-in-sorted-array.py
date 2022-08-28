# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         l,r = 0, len(nums)-1
#         res=[]
        
#         while l <= r:
#             mid = l + (r - l) //2
#             if nums[mid] == target:
#                 if nums[mid-1]!=nums[mid]:
#                     res.append(mid)
#                 if nums[mid]!=nums[mid+1]:
#                     res.append(mid)

#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return res
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:

                start = m
                while start >= 0 and nums[start] == target:
                    start -= 1
                

                end = m
                while end < len(nums) and nums[end] == target:
                    end += 1
                return [start+1, end-1]

        return [-1, -1]

