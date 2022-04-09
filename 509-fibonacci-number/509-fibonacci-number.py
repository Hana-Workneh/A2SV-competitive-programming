class Solution:
    def fib(self, n: int) -> int:
        memo={1:1,0:0}
        def fibo(i):
            if i in memo:
                return memo[i]
            memo[i] = fibo(i-1) + fibo(i-2)
            return memo[i]

        return fibo(n)