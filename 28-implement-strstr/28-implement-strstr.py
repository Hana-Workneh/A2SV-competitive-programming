class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if h < n: 
            return -1
        for i in range(h-n +1):
            print(i)
            if haystack[i:i + n] == needle:
                return i
        return -1
            

   


