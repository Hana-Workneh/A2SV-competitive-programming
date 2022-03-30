class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        charPos =  {}
        res = []
        left, right = 0, 0
        
        for i, c in enumerate(S):      
            charPos[c] = i
        for i, c in enumerate(S):
            right = max(right, charPos[c])
            if right == i:
                res.append(right - left + 1)
                left = i + 1
        return res
        