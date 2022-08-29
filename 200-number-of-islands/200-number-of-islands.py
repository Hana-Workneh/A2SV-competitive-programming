class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        def find_islands(m, n):
            grid[m][n] = '*'
            
            if m >= 1 and grid[m-1][n] == '1':
                find_islands(m-1, n)
            if m < len(grid) - 1 and grid[m+1][n] == '1':
                find_islands(m+1, n)
            if n >= 1 and grid[m][n-1] == '1':
                find_islands(m, n-1)
            if n < len(grid[0]) - 1 and grid[m][n+1] == '1':
                find_islands(m, n+1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    find_islands(i, j)
        
        return islands