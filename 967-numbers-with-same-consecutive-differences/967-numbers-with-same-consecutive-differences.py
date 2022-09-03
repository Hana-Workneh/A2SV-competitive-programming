class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        
        def comb(num, leni):
            if leni == n:
                res.append(num)
                return
            
            if k == 0:
                comb(num * 10 + num % 10, leni + 1)
                return
            
            if num % 10 + k <= 9:
                comb(num * 10 + num % 10 + k, leni + 1)
                
            if num % 10 - k >= 0:
                comb(num * 10 + num % 10 - k, leni + 1)
                
            return
        
        for i in range(1, 10):
            comb(i, 1)
            
        return res
        