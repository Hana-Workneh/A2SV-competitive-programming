class Solution:
    def romanToInt(self, s: str) -> int:
        romains_char_number = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        romains_substractable_char = {'CM':900, 'CD': 400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
        
        i = len(s)-1
        res = 0

        while i>=0:

            tmp = s[i-1:i+1]
            if tmp in romains_substractable_char:
                res += romains_substractable_char[tmp]
                i-=2
            else:
                res += romains_char_number[s[i]]
                i-=1
        return res