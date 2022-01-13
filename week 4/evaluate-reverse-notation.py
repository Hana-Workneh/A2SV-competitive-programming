#leetcode
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op =["+","-","*","/"]
        stack=[]
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            if i in op and len(stack) != 0:
                postfix=0
                temp=stack.pop() 
                temp2=stack.pop() 
                if i == "+":
                    postfix=temp + temp2
                elif i == "-":
                    postfix=temp2 - temp
                elif i == "*":
                    postfix=temp * temp2
                elif i == "/":
                    if temp * temp2 > 0 :
                        postfix = temp2 // temp
                    else:
                        postfix = (temp2 + (-temp2 % temp)) // temp
                stack.append(postfix)
        return stack.pop()
