class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rowMax, colMax = len(heights), len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        myMap, minHeap= [[sys.maxsize for _ in range(colMax)] for _ in range(rowMax)], [(0,0,0)]
        myMap[0][0] = 0

        while(minHeap):
            maxDiff, row, col = heapq.heappop(minHeap)
            if(row == (rowMax - 1) and col == (colMax - 1)):
                return(maxDiff)
            for shiftRow, shiftCol in directions:
                newRow, newCol = row + shiftRow, col + shiftCol
                if(0 <= newRow < rowMax and 0 <= newCol < colMax):
                    newDiff = max(maxDiff, abs(heights[row][col] - heights[newRow][newCol]))
                    if(newDiff < myMap[newRow][newCol]):
                        myMap[newRow][newCol] = newDiff
                        heapq.heappush(minHeap, (newDiff, newRow, newCol))
        return(-1)
