class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        result = [None] * len(questions)
        return self.mostPointsHelper(questions, 0, result)


    def mostPointsHelper(self, questions, ind, result):
        if ind >= len(questions):
            return 0
        if result[ind] is not None:
            return result[ind]
        maxPoints = max(questions[ind][0] + self.mostPointsHelper(questions, ind + questions[ind][1] + 1, result),
                        self.mostPointsHelper(questions, ind+1, result))
        result[ind] = maxPoints
        return maxPoints