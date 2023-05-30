class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue, rowMax, colMax = deque(), len(grid), len(grid[0])
        directions, visited = [[1,0], [0,1], [-1,0], [0,-1]], set()

        def DFS(startRow, startCol):
            nonlocal visited, visited
            visited.add((startRow, startCol))
            for shiftVirt, shiftHor in directions:
                newRow, newCol = startRow + shiftVirt, startCol + shiftHor
                if(0 <= newRow < rowMax and 0 <= newCol < colMax and (newRow, newCol) not in visited):
                    if(grid[newRow][newCol] == 1):
                        DFS(newRow, newCol)
                    elif(grid[newRow][newCol] == 0):
                        queue.append((newRow, newCol, 1))
                        grid[newRow][newCol] = 2
        
        def findOne():
            for row in range(rowMax):
                for col in range(colMax):
                    if(grid[row][col] == 1):
                        DFS(row, col)
                        return()
        findOne()

        while(queue):
            startRow, startCol, steps = queue.popleft()
            for shiftVirt, shiftHor in directions:
                newRow, newCol = startRow + shiftVirt, startCol + shiftHor
                if(0 <= newRow < rowMax and 0 <= newCol < colMax):
                    if(grid[newRow][newCol] == 1 and (newRow, newCol) not in visited):
                        return(steps)
                    elif(grid[newRow][newCol] == 0):
                        queue.append((newRow, newCol, steps + 1))
                        grid[newRow][newCol] = 2
        return(-1)