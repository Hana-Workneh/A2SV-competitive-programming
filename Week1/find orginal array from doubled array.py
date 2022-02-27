class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        
        changed.sort()
        doubled = defaultdict(int)
        res = []
        for i in range(len(changed)):
            if doubled[changed[i]] > 0 :
                res.append(changed[i] // 2)
                doubled[changed[i]] -= 1
            else:
                doubled[changed[i]*2] += 1
        
        if len(res) == len(changed)// 2:
            return res
        else :
            return []
