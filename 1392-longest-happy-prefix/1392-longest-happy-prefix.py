class Solution:
    def longestPrefix(self, s: str) -> str:
        result = [0] * len(s)
        i,j = 0, 1
        
        while j < len(s) and i >= 0:
            if s[i] == s[j]:
                result[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    result[j] = 0
                    j += 1
                else:
                    i = result[i - 1]
                        
        return s[:result[-1]]