class Solution:
    memo={}
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        if self.memo.get(n, None) != None:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]