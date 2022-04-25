class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree, graph  = [0]*numCourses, defaultdict(list)
        for dist, source in prerequisites:
            graph[source].append(dist)
            indegree[dist] += 1
        
        queue = deque([i for i in range(numCourses) if not indegree[i]])
        count = len(queue)
        
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                indegree[next_course] -=1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    count += 1
                    
        return count == numCourses