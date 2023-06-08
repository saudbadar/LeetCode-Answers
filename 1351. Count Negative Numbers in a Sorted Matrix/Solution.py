class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        negatives = 0
        col = 0
        for row in range(ROWS - 1, -1, -1):
            while col < COLS and grid[row][col] >= 0:
                col += 1
            negatives += COLS - col
        return negatives