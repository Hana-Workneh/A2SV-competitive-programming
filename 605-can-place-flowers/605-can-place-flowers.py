class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: 
            return True
        N = len(flowerbed)
        for i, f in enumerate(flowerbed):
            if (i == 0 and i + 1 >= N and flowerbed[i] == 0) or \
            (i == 0 and i + 1 < N and flowerbed[i + 1] == 0 and flowerbed[i] == 0) or \
            (i - 1 >= 0 and i + 1 < N and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0) or \
            (i == N - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0):
                n -= 1
                flowerbed[i] = 1
            if n == 0:
                return True
        return False