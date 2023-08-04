class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        rowMax, colMax, moves = n, n, [[1,2],[2, 1],[-1,2],[2,-1],[1,-2],[-2,1],[-1,-2],[-2,-1]]
        DP, ret = [[0 for _ in range(rowMax)] for _ in range(colMax)], 0
        DP[row][column] = 1

        for idx in range(k):
            newDP = [[0 for _ in range(rowMax)] for _ in range(colMax)]
            for row in range(rowMax):
                for col in range(colMax):
                    if(DP[row][col] != 0):
                        for move in moves:
                            newRow, newCol = row + move[0], col + move[1]
                            if(0 <= newRow < rowMax and 0 <= newCol < colMax):
                                newDP[newRow][newCol] += (DP[row][col] / 8)
            DP = newDP
        for row in range(rowMax):
            for col in range(colMax):
                ret += DP[row][col]
        return(ret)