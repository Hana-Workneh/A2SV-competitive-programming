class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record=[]
        for i in ops:
            if i not in "CD+":
                record.append(int(i))
            else:
                if i == '+':
                    record.append(record[-1] + record[-2])
                elif i == 'D':
                    record.append(2 * record[-1])
                elif i == 'C':
                    record.pop()           
        return sum(record)
