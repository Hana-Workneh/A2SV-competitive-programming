class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, curr = [], ""
        for i in s:
            if i=='(':
                stack.append(curr)
                curr=""
            elif i==')':
                curr=curr[::-1]
                curr=stack.pop()+curr
            else:
                curr+=i
        return curr
