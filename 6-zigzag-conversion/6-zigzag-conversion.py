class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        index,step = 0,1
        arr = [""] * numRows
        
        for str in s: 
            arr[index] += str
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1                             
            index += step
        return "".join(arr)