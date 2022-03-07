#hackerrank
def heappeak(heap):
    s = heapq.heappop(heap)
    heapq.heappush(heap, s)
    
    return s

def cookies(k, A):
    heapq.heapify(A)
    iterCount = 0
    
    while heappeak(A) < k:
        if len(A) <= 1 and heappeak(A) < k:
            return -1
          
        s1 = heapq.heappop(A)
        s2 = heapq.heappop(A)
        heapq.heappush(A, s1 + 2 * s2)
        iterCount += 1
        
    return iterCount
