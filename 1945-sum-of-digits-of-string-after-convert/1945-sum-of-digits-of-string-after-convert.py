class Solution:
    def getLucky(self, s: str, k: int) -> int:
        x = ''
        for i in s:
            x += str(ord(i) - 96)
        while k > 0:
            z = 0
            for i in x:
                z += int(i)
            x = str(z)
            k -= 1
        return x