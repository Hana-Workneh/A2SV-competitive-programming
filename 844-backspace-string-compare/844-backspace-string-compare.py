class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            
            if s[i] == "#":
                if len(stack1) == 0:
                    continue
                stack1.pop()
            else:
                stack1.append(s[i])
        for i in range(len(t)):
            
            if t[i] == "#":
                if len(stack2) == 0:
                    continue
                stack2.pop()
            else:
                stack2.append(t[i])
        if stack1 == stack2:
            return True
        return False