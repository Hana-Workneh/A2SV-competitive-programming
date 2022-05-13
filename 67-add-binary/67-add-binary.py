class Solution:
    def addBinary(self, a: str, b: str) -> str:
       
        a, b = a[::-1], b[::-1]
        
        num_a=0
        for i in range(len(a)):
            num_a += int(a[i])*2**i
        
        num_b = 0
        for i in range(len(b)):
            num_b += int(b[i])*2**i        
        
        sum = num_a + num_b
        
        if sum==0: 
            return '0'
        
        binary=''
        while sum > 0:
            binary += str(sum % 2)
            sum //= 2
        return binary[::-1]