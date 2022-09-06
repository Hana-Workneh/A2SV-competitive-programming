class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        d = {}
        chain = 0
        left=0
        
        for i,a in enumerate(s):
            if(a not in d):
                chain += 1
            
            else:
                if(d[a] < (i-chain)): 
                    chain += 1
                else: 
                    chain -= (d[a]-left)
                    left = d[a]+1
            if(chain > longest): longest = chain   
            d[a] = i
        return longest