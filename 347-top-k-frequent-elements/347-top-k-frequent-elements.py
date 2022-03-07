class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        arr=[(-count[x],x) for x in count.keys()]
        heapq.heapify(arr)
        res=[]
        while k > 0:
            res.append(heapq.heappop(arr))
            k-=1 
        return [j for i,j in res]