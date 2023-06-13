class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowMax, colMax, myDict, ret = len(grid), len(grid[0]), {}, 0

        for row in range(rowMax):
            myDict[tuple(grid[row])] = myDict.get(tuple(grid[row]), 0) + 1
        
        for col in range(colMax):
            lst = []
            for row in range(rowMax):
                lst.append(grid[row][col])
            ret += myDict.get(tuple(lst), 0)
        return(ret)