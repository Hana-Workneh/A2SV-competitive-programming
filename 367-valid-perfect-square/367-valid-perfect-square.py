class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search solution
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            else:
                if mid * mid > num:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
    