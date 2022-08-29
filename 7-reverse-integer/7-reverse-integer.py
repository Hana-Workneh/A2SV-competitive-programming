class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        r = x
        x = abs(x)
        while x>0:
            n = (n*10) + x%10
            x=x//10
            
        ans = -n if r<0 else n
        if ans<0 and ans<-2**31:
            return 0
        
        if ans>2**31-1:
            return 0
        return ans
        