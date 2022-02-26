class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(map(int, list(num)))
        for k in range(k):
            for i in range(len(num)):
                if (i == len(num)-1) or (num[i] > num[i+1]):
                    num.pop(i)
                    break
            while num and (num[0] == 0):
                num.pop(0)
            if len(num)==0:
                return "0"
        num=map(str, num)
        return "".join(num)