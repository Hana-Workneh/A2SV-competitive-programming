class Solution:
    def concatenatedBinary(self, n: int) -> int:
        final_number = ''
        for x in range(1, n+1):
            final_number += bin(x)[2:]
        
        return int(final_number, 2) % (10**9 + 7)