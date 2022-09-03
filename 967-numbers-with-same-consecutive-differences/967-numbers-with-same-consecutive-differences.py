class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans = []

        def getNumbers(size, x, num):
            if size == 0:
                ans.append(num)
                return

            if x + k < 10:
                getNumbers(size - 1, x + k, (num * 10) + (x + k))
            if k != 0 and x - k >= 0:
                getNumbers(size - 1, x - k, (num * 10) + (x - k))

        for i in range(1, 10):
            getNumbers(n - 1, i, i)

        return ans