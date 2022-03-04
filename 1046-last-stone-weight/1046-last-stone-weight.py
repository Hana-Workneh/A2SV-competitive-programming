class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return -1*stones[0]
        if len(stones) == 2 and stones[0] == stones[1]:
            return 0
        while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones) 
            if x!=y:
                heapq.heappush(stones,x-y)
            if len(stones) == 2 and stones[0] == stones[1]:
                return 0
        for i in range(len(stones)):
            stones[i] *= -1        
            return stones[i]