
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for i in graph[node]:
                if i not in vis:
                    vis.add(i)
                    dfs(i)
        graph = collections.defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i !=j and isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
        vis = set()
        count = 0
        for i in range(1,n+1):
            if i not in vis:
                vis.add(i)
                count += 1
                dfs(i)
        return count
