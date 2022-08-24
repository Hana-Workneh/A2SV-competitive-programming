class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[[],[]]
        nums1,nums2=set(nums1),set(nums2)
        for i in nums1:
            if i not in nums2:
                answer[0].append(i)
        for i in nums2:
            if i not in nums1:
                answer[1].append(i)
        return answer