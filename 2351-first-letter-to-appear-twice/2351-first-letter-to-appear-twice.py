class Solution:
    def repeatedCharacter(self, s: str) -> str:
        Set = set()
        for i in s:
            if i in Set: return i
            Set.add(i)