class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lengthOne, lengthTwo = len(word1), len(word2)
        DP = [[0 for _ in range(lengthOne + 1)] for _ in range(lengthTwo + 1)]

        for row in range(1, lengthTwo + 1):
            for col in range(1, lengthOne + 1):
                if(word1[col - 1] == word2[row - 1]):
                    DP[row][col] = 1 + DP[row - 1][col - 1]
                else:
                    DP[row][col] = max(DP[row - 1][col], DP[row][col - 1])
        return(lengthOne + lengthTwo - (2 * DP[-1][-1]))