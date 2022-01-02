#leetcode
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res=[]
        s=intervals[0][0]
        e=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= e:
                e=max(e,intervals[i][1])
            else:
                res.append([s,e])
                e=intervals[i][1]
                s=intervals[i][0]     
        res.append([s,e])
        return res              
