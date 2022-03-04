class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap  = []
        self.min_count = 0
        self.max_count = 0
        self.median = 0
    
    def addNum(self, num: int) -> None:
        if self.min_count == 0 and self.max_count ==0:
            heapq.heappush(self.max_heap, -1 *num)
            self.median = num
            self.max_count +=1 
            return
        else:
            if num > self.median:
                heapq.heappush(self.min_heap, num)
                self.min_count += 1
            else:
                heapq.heappush(self.max_heap, -1 *num)
                self.max_count += 1
                
        if abs(self.max_count - self.min_count) > 1:
            if self.min_count > self.max_count:
                heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))
                self.min_count -=1
                self.max_count +=1
            else:
                heapq.heappush(self.min_heap, -1 *heapq.heappop(self.max_heap))
                self.min_count +=1  
                self.max_count -=1      
        
        if abs(self.max_count - self.min_count) % 2==1:
            if self.min_heap and  self.min_count > self.max_count:
                self.median = self.min_heap[0]
            if self.max_heap and self.min_count < self.max_count:
                self.median = -1 * self.max_heap[0]
        else:
            self.median = (-1 * self.max_heap[0] + self.min_heap[0])/2
                
    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()