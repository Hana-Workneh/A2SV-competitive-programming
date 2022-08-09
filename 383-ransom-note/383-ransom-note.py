class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = list(ransomNote)
        mg = list(magazine)
        count = 0
        for i in range(len(rn)):
            if rn[i] in mg:
                ind= mg.index(rn[i])
                mg.pop(ind)
                count += 1
        if len(rn) == count:
            return True
        return False
            