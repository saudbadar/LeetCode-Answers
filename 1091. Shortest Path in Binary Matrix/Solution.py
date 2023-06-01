class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowMax, colMax = len(grid), len(grid[0])
        direction = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        queue = collections.deque()
        if(grid[0][0] == 0):
            queue.append((0,0,1))
        while(queue):
            startRow, startCol, step = queue.popleft()
            if(startRow == (rowMax - 1) and startCol == (colMax - 1)):
                return(step)
            for move in direction:
                newRow, newCol = startRow + move[0], startCol + move[1]
                if(0 <= newRow < rowMax and 0 <= newCol < colMax and grid[newRow][newCol] == 0):
                    grid[newRow][newCol] = 1
                    queue.append((newRow, newCol, step + 1))
        return(-1)