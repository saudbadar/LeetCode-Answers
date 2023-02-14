class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lenOne, lenTwo = len(text1), len(text2)
        DP = [[0 for _ in range(lenOne + 1)] for _ in range(lenTwo + 1)]

        for row in range(1, lenTwo + 1):
            for col in range(1, lenOne + 1):
                if(text1[col - 1] == text2[row - 1]):
                    DP[row][col] = DP[row - 1][col - 1] + 1
                else:
                    DP[row][col] = max(DP[row - 1][col], DP[row][col - 1])
        return(DP[-1][-1])