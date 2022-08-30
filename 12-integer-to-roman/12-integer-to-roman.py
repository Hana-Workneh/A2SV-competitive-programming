class Solution:
    roman_number = ''

    def intToRoman(self, num: int) -> str:
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        symbols = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        for value, symbol in zip(values, symbols):
            num = self.convertNumToLetter(num, value, symbol)

        return self.roman_number
        
    def convertNumToLetter(self, num: int, value: int, symbol: str) -> int:
        out = num // value
        self.roman_number += symbol * out
        return num - (out * value)