class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabets = []
        s = list(s)
        
        for i in range(len(s)):
            
            if ord(s[i])>=97 and ord(s[i])<=122 or ord(s[i])>=48 and ord(s[i])<=57 :
                alphabets.append(s[i])

        alphabets = "".join(alphabets)     
        rev = alphabets[::-1]
            
        if  rev == alphabets:
            print(rev, alphabets)
            return True
        
        return False
      