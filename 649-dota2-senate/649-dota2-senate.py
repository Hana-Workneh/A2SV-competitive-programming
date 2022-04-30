class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        :type senate: str
        :rtype: str
        """
        s = list(senate)
        i = j = 0
        while True:
            while i < len(s) and s[i] != 'R': # find the next Radiant representative
                i += 1
            if i == len(s):
                return 'Dire'

            while j < len(s) and s[j] != 'D': # find the next Dire representative
                j += 1
            if j == len(s):
                return 'Radiant'

            if i < j:     # after voting, move the voted representative to the end of the list
                s[j] = 'X'
                s.append('R')
            else:
                s[i] = 'X'
                s.append('D')

            i += 1
            j += 1