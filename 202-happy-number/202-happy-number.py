class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = sum([int(x)**2 for x in str(n)])
            if n in seen:
                return False
            seen.add(n)
            if n == 1:
                return True