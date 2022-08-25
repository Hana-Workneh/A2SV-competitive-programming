class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars={}
        length=0
        for char in s:
            if char in chars:
                chars[char]=chars[char]+1
            else:
                chars[char]=1

        for char in chars:
            length+=chars[char]//2*2

        if length<len(s):
            length+=1
        return length