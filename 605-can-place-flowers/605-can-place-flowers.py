class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, N = 0, len(flowerbed)       
        if N == 1:
            if flowerbed[0]==0:
                count += 1
                n  -= 1
            
        else:
            if flowerbed[1] == flowerbed[0] == 0:
                flowerbed[0] = 1
                count += 1
            if flowerbed[N - 2] == flowerbed[N - 1] == 0:
                flowerbed[N - 1] = 1
                count += 1
                
            for i in range(1, N - 1):
                if flowerbed[i] == flowerbed[i + 1] == flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n