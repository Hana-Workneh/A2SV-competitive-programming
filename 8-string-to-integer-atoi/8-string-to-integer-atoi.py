class Solution:

    def myAtoi(self, s: str) -> int:
        def check( temp_res: int):
            if temp_res > (2 ** 31) - 1:
                return (2 ** 31) - 1
            elif temp_res < (-2 ** 31):
                return (-2 ** 31)
            else:
                return temp_res
        s = s.strip()
        if len(s) == 0:
            return 0
        flag = -1 if s[0] == "-" else 1
        s = s[1:] if (s[0] == "-" or s[0] == "+") else s
        res=0
        for i in s:
            if "0" <= i <= "9":
                res *= 10
                res+=int(i)
                res = flag*check(flag*res)
            else:
                break
        return check(flag*res)