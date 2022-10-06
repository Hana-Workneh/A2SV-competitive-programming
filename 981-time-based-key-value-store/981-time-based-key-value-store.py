class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.dic:
            searchList = self.dic[key]
            l, r = 0, len(searchList) - 1
            while l <= r:
                m = l + (r - l) // 2
                if searchList[m][0] <= timestamp:
                    res = searchList[m][1]
                    l = m + 1
                else:
                    r = m - 1
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)