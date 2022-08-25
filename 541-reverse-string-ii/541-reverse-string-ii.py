class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        m = ''
        for i in range(0,len(s),2*k):
            m = s[i:i+k]
            s =s[:i] +m[k::-1] + s[i+k:]
        return s