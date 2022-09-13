class Solution:
    def validUtf8(self, data):
        state = -1
        cnt = 0 
        for d in data :
            if state == -1 : # setting type
                if d < 128 :
                    state = 1 
                elif 192 <= d < 224 :
                    state = 2 
                elif 224 <= d < 240 :
                    state = 3 
                elif 240 <= d < 248 :
                    state = 4 
                else :
                    return False 
                cnt = state-1
            else :
                if d < 128 or d >= 192 :
                    return False 
                cnt -= 1 


            if cnt == 0 :
                state = -1 


        return cnt == 0