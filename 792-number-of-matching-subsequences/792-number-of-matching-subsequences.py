class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        memo = {}
        for word in words:
            if word in memo:
                if memo[word]:
                    count += 1
                continue
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    j += 1
                    i += 1
                else:
                    j += 1
            if i == len(word):
                count += 1
            memo[word] = (i == len(word))
        return count
