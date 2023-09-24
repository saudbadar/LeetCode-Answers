class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        DP = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
        DP[0][0] = poured

        for i in range(query_row):
            for j in range(len(DP[i])):
                temp = (DP[i][j] - 1) / 2
                if(temp > 0):
                    DP[i + 1][j] += temp
                    DP[i + 1][j + 1] += temp
        return(DP[query_row][query_glass] if DP[query_row][query_glass] <= 1 else 1)