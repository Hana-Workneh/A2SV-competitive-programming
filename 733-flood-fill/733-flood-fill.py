class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited=set()
        visited.add((sr,sc))
        startColor = image[sr][sc]
        insideMatrix = lambda row,col: 0 <= row < len(image) and 0 <= col < len(image[0])
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(row,col):
            image[row][col]= newColor
            visited.add((row,col))
    
            for direction in directions:
                row2, col2 = row + direction[0], col + direction[1]
                if (row2,col2) in visited or not insideMatrix(row2,col2) or image[row2][col2] != startColor:
                    continue
                dfs(row2,col2)
                
            return image
        image = dfs(sr,sc)
        return image