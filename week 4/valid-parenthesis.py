#leetcode
class Solution:
    def isValid(self, s: str) -> bool:
        par=dict()
        par["("]=')'
        par['{']='}'
        par['[']=']'
        stack = []
        for i in s:
            if i in par.keys():
                stack.append(i)
            elif len(stack) == 0 or i != par[stack.pop()]:
                return False
        return len(stack) == 0
