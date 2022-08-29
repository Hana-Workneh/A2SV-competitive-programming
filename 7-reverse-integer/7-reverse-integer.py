class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        p = s[::-1]
        if "-" in s:
            num = p.replace("-","")
            
            result =  (int(num)-int(num)*2)
            
        else:
            result =  int(p)
            
        if result > -2**31-1 and result < 2**31-1:
            
            return result
        else:
            return 0