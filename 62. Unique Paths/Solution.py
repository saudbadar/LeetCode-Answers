class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[0 for _ in range(n)] for _ in range(m)]

        def DFS(startRow, startCol):
            nonlocal DP
            paths = 0
            if((startRow == (m - 1)) and (startCol == (n - 1))):
                return(1)
            for shiftRow, shiftCol in [[0,1], [1,0]]:
                newRow, newCol = startRow + shiftRow, startCol + shiftCol
                if(0 <= newRow < m and 0 <= newCol < n):
                    if(DP[newRow][newCol] == 0):
                        paths += DFS(newRow, newCol)
                    else:
                        paths += DP[newRow][newCol]
            DP[startRow][startCol] = paths
            return(paths)
        
        return(DFS(0,0))