#leetcode 
class Solution:
    def sortSentence(self, s: str) -> str:
        res=[]
        splited=s.split()
        for i in splited:
            splited.sort(key = lambda x:x[-1])   
        for i in range(len(splited)):
            temp=str(splited[i])
            tempFinal=temp[:-1]
            res.append(tempFinal)
        res=" ".join(res)
        return res
