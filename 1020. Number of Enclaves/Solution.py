class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited, ret, rowMax, colMax = set(), 0, len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def recursion(startRow, startCol):
            nonlocal visited, seenEdge, depth
            depth += 1
            if(startRow == 0 or startRow == (rowMax - 1) or startCol == 0 or startCol == (colMax - 1)):
                seenEdge = True
            visited.add((startRow, startCol))
            for shiftRow, shiftCol in directions:
                newRow, newCol = startRow + shiftRow, startCol + shiftCol
                if(0 <= newRow < rowMax and 0 <= newCol < colMax and (newRow, newCol) not in visited and grid[newRow][newCol] == 1):
                    recursion(newRow, newCol)
        
        for row in range(rowMax):
            for col in range(colMax):
                seenEdge, depth = False, 0
                if(grid[row][col] == 1 and (row, col) not in visited):
                    recursion(row, col)
                    if(not seenEdge):
                        ret += depth
        return(ret)