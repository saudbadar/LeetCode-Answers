class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        cols = [0] * n
        rows = [0] * m
        for i in range(m):
            for j in range(n):
                v = grid[i][j] if grid[i][j] == 1 else -1
                rows[i] += v
                cols[j] += v
        for i in range(m):
            for j in range(n):
                grid[i][j] = rows[i] + cols[j]
        return grid