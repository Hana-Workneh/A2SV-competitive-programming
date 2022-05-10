class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest= min(strs, key=len)
        length = len(shortest)
        
        for word in strs:
            if shortest not in word[:length]:
                i = 0
                while i < length:
                    if shortest[i] != word[i]:
                        if index == 0: 
                            return ""
						
                        shortest = shortest[:i]
                        break
                    i += 1
        return shortest