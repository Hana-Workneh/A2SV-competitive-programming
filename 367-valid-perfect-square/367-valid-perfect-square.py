class Solution(object):
    def isPerfectSquare(self, num):
        x = num**0.5
        if(int(x) == x):
            return True
        return False