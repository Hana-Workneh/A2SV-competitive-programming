class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = ""
        palindrome = list(palindrome)
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                palindrome[i] = "a"
                ans = "".join(palindrome)
                break
            elif i == len(palindrome)//2 - 1:
                palindrome[-1] = "b"
                ans = "".join(palindrome)
                
        return ans