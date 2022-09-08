class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=int(dividend/divisor)
        if a>2147483647:
            return 2147483647
        elif a<-2147483647:
            return -2147483648
        else:
            return a