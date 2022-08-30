class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=len(matrix)
        for i in range(l):
            for j in range(i+1,l):
                if i != j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i,row in enumerate(matrix):
            matrix[i]=row[::-1]
        return matrix