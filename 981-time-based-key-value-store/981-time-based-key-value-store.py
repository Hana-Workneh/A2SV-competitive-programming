class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
       
        l = self.d[key]
        if timestamp < l[0][0]:
            return ""
        left, right = 0, len(l)-1
        while left < right:
            mid = (left + right)
            if self.d[key][mid][0] == timestamp:
                return self.d[key][mid][1] 
            elif self.d[key][mid][0] < timestamp:
                left = mid
            else:
                right = mid-1
        return self.d[key][left][1] 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)