class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i, s, cash = dict()):
            if i in cash:
                return cash[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            split1 = dfs(i + 1, s)
            cash[i + 1] = split1
            if i < len(s) - 1 and int(s[i:i+2]) < 27:
                split2 = dfs(i + 2, s)
                cash[i + 2] = split2
                cash[i] = split1 + split2
                return split1 + split2
            return split1
        return dfs(0, s)