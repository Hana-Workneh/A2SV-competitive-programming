#leetcode
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphicS = dict()
        isomorphicT= dict()
        for i, j  in zip(s, t):
            if ((i in isomorphicS and isomorphicS[i] != j) or (j in isomorphicT and isomorphicT[j] != i)):
                return False
            isomorphicS[i] = j
            isomorphicT[j] = i    
        return True


