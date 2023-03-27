class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        matrix = [[sys.maxsize] * col for _ in range(row)]
        matrix[row - 1][col - 1] = grid[row - 1][col - 1]
        
        def dfs(tempRow, tempCol):
            while(tempRow + 1 < row):
                if(matrix[tempRow + 1][tempCol] != sys.maxsize):
                    matrix[tempRow][tempCol] = min(matrix[tempRow][tempCol], grid[tempRow][tempCol] + matrix[tempRow + 1][tempCol])
                    break
                else:
                    dfs(tempRow + 1, tempCol)
            while(tempCol + 1 < col):
                if(matrix[tempRow][tempCol + 1] != sys.maxsize):
                    matrix[tempRow][tempCol] = min(matrix[tempRow][tempCol], grid[tempRow][tempCol] + matrix[tempRow][tempCol + 1])
                    break
                else:
                    dfs(tempRow, tempCol + 1)
        dfs(0,0)
        return(matrix[0][0])