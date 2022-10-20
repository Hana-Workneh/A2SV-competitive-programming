
val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
class Solution:
    def intToRoman(self, N: int) -> str:
        ans = ""
        for value in range(len(val)):
            while N >= val[value]:
                ans += rom[value]
                N -= val[value]
        return ans