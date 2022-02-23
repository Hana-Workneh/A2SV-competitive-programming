class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end =0, len(numbers) - 1
        temp, temp2 = 1, len(numbers)
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [temp, temp2]
            elif numbers[start] + numbers[end] < target:
                start += 1
                temp += 1
            elif numbers[start] + numbers[end] > target:
                end -= 1
                temp2 -= 1