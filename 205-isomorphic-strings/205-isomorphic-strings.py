class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        di = {}
        se = set()
        for i in range(len(s)):
            if t[i] in se and s[i] not in di:
                return False
            if s[i] not in di:
                di[s[i]] = t[i]
                se.add(t[i])
            elif t[i] != di[s[i]]:
                return False
        return True