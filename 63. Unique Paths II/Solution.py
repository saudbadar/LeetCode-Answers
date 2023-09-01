class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rowMax, colMax = len(obstacleGrid), len(obstacleGrid[0])
        DP, moves = [[-1 for _ in range(colMax)] for _ in range(rowMax)], [[1,0], [0,1]]

        def recursion(row, col):
            nonlocal DP
            paths = 0
            if(row == (rowMax - 1) and col == (colMax - 1)):
                return(1)
            for rowShift, colShift in moves:
                newRow, newCol = row + rowShift, col + colShift
                if(newRow < rowMax and newCol < colMax and obstacleGrid[newRow][newCol] != 1):
                    if(DP[newRow][newCol] != -1):
                        paths += DP[newRow][newCol]
                    else:
                        paths += recursion(newRow, newCol)
            DP[row][col] = paths
            return(paths)
        return(recursion(0,0) if obstacleGrid[0][0] == 0 else 0)