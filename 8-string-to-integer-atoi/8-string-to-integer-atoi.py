class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.strip()
        if s == "" or s =="0":
            return 0
        new_s = ""
        if s[0] == "-":
            sign = -1
            new_s = s[1:]
        elif s[0] == "+":
            new_s = s[1:]
        else:
            new_s = s
        if new_s == "" or new_s[0] == "+" or new_s[0] == "-" or not new_s[0].isnumeric() :
            return 0
        numbers = ""    
        for num in new_s:
            if num.isnumeric():
                numbers += num
            else:
                break
        if int(numbers) * sign > 2**31 -1:
            return 2**31 -1
        elif int(numbers) *sign < - 2**31:
            return  2**31 * sign

        return int(numbers) * sign
