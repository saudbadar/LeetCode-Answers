class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        DP = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            DP[i][i] = 1
        
        for a in range(2, length + 1):
            for row in range(length - a + 1):
                col = row + a - 1
                if(s[row] == s[col]):
                    DP[row][col] = 2 + DP[row + 1][col - 1]
                else:
                    DP[row][col] = max(DP[row + 1][col], DP[row][col - 1])
        return(length - DP[0][length - 1])
