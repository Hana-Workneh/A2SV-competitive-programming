class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                nums.append(matrix[i][j])
        nums.sort()
        while len(nums) > k :
            nums.pop()
        return nums[-1]