class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in arr:
            if i==0 and arr.count(0)>1:
                return True
                    
            if i!=0 and 2*i in arr:
                return True
        return False
            