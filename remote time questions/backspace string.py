class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
            stack = []
            stack2 = []
            for i in s:
                if i == '#':
                    if len(stack)==0:
                        continue
                    else:
                        stack.pop()
                else:
                    stack.append(i)
            for i in t:
                if i == "#":
                    if len(stack2)==0:
                        continue
                    else:
                        stack2.pop()
                else:
                    stack2.append(i)

            return stack == stack2
