class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:     
            stack=[]
            
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    if nums1[i] == nums2[j]:
                            temp = j
                            
                for i in range(temp, len(nums2)):
                        if nums2[i] > nums2[temp]:
                            stack.append(nums2[i])
                            break
                        elif i == len(nums2)-1:
                            stack.append(-1)
                        else:
                            continue
                            
            return stack
        
       #OR 
        
        """ using monotonic stack """
        
    class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:     
        dicti = {}
        stack = [nums2[0]]
        for i in nums2:
            while stack and i >= stack[-1]:
                dicti[stack.pop()] = i
            stack.append(i)
        for j in stack:
            dicti[j] = -1
        return [dicti[j] for j in nums1]
