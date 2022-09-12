class Solution:
    def bagOfTokensScore(self, token: List[int], power: int) -> int:
        l=0
        r = len(token)-1
        score=0
        token.sort()
        ans=0
        while l<=r:
            if power>=token[l]:
                power -= token[l]
                score+=1
                ans = max(ans,score)
                l+=1
            elif score>=1:
                power += token[r]
                score -=1
                r-=1
            else:
                break
        return ans