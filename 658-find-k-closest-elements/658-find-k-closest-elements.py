import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for num in arr:
            distance = abs(num - x)
            heapq.heappush(heap, [distance, num])
        
        result = []
        for i in range(k):
            distance, num = heapq.heappop(heap)
            result.append(num)
        
        return sorted(result)