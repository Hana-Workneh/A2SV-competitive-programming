class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            nums = []
            k = i
            j = 0
            while k < rows and j < cols:
                nums.append(mat[k][j])
                j += 1
                k += 1
            # print(nums)
            nums = sorted(nums)
            k = i
            j = 0
            while k < rows and j < cols:
                mat[k][j] = nums[j]
                j += 1
                k += 1
        
        for i in range(1, cols):
            nums = []
            k = 0
            j = i
            while k < rows and j < cols:
                nums.append(mat[k][j])
                j += 1
                k += 1
            # print(nums)
            nums = sorted(nums)
            k = 0
            j = i
            while k < rows and j < cols:
                mat[k][j] = nums[k]
                j += 1
                k += 1
                
        return mat