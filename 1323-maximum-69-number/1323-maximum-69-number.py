class Solution:
    def maximum69Number (self, num: int) -> int:
        if num==9999:
            return num
        else:
            num=list(map(int,list(str(num))))
            # num.sort(reverse=True)
            for i in range(len(num)):
                if num[i]==9:
                    continue
                elif num[i]==6:
                    num[i]=9
                    break
        num=map(str,num)
        return ''.join(num)