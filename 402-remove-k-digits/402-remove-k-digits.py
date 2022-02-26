class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(map(int, list(num)))
        for i in range(k):
            for j in range(len(num)):
                if (j == len(num)-1) or (num[j] > num[j+1]):
                    num.pop(j)
                    break
            while num and (num[0] == 0):
                num.pop(0)
            if len(num)==0:
                return "0"
        num=map(str, num)
        return "".join(num)