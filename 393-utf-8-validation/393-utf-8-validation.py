class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if data[0]>247:return False
        def b(x):
            bx=-1
            for i in range(7,3,-1):
                if x>>i&1:
                    bx+=1
                else:break
            return bx
        
        bx=0
        N=len(data)
        for i in range(N):
            if bx>0:
                if 128>data[i] or data[i]>191:return False
                bx-=1
            else:
                if data[i]>127:
                    bx=b(data[i])
                    if bx==0 or bx>N-1:return False
                    
        return True