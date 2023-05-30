class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        DP = [0 for _ in range(length + 1)]

        for idx in range(length - 1, -1, -1):
            point, brain, nextVal = questions[idx][0], questions[idx][1], 0
            if((idx + brain) < length):
                nextVal = DP[idx + brain + 1]
            DP[idx] = max(point + nextVal, DP[idx + 1])
        return(DP[0])