class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rowMax, colMax, mySet, ret = len(grid), len(grid[0]), set(), 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for row in range(rowMax):
            for col in range(colMax):
                if(grid[row][col] == 0):
                    mySet.add((row, col))
        
        def search(startRow, startCol):
            nonlocal seenEdge, mySet
            if(startRow == 0 or startRow == (rowMax - 1) or startCol == 0 or startCol == (colMax - 1)):
                seenEdge = True
            for move in directions:
                newRow, newCol = startRow + move[0], startCol + move[1]
                if(0 <= newRow < rowMax and 0 <= newCol < colMax and (newRow, newCol) in mySet):
                    mySet.remove((newRow, newCol))
                    search(newRow, newCol)
        while(mySet):
            rowStart, colStart = mySet.pop()
            seenEdge = False
            search(rowStart, colStart)
            if(not seenEdge):
                ret += 1
        return(ret)