class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacencyList = defaultdict(list)
        for u,v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)
            
        queue = [source]
        visited=set([source])
        while queue:
            node = queue.pop(0)
            
            if node == destination:
                return True
            
            for neighbour in adjacencyList[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    
        return False 