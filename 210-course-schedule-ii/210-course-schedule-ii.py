class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = list()
        indegree = [0] * numCourses
        for p in prerequisites:
            indegree[p[0]] += 1
        
        s = [i for i in range(numCourses) if indegree[i] == 0]
        
      
        if len(s) == 0:
            return [] 
        
        while s:
            course = s.pop()
            res.append(course)
            
            for p in prerequisites:
                if course == p[1]:
                    indegree[p[0]] -= 1
                    
                    if indegree[p[0]] == 0:
                        s.append(p[0])
   
        for i in range(numCourses):
            if indegree[i] != 0:
                return []
        
        return res