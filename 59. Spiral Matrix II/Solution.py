class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret, direction = [[0 for _ in range(n)] for _ in range(n)], [[0,1], [1,0], [0,-1], [-1,0]]
        startRow, startCol, move = 0, 0, 0
        for i in range(1, pow(n,2) + 1):
            ret[startRow][startCol] = i
            newRow, newCol = startRow + direction[move % 4][0], startCol + direction[move % 4][1]
            if(newRow >= n or newRow < 0 or n <= newCol or newCol < 0 or ret[newRow][newCol] != 0):
                move += 1
            startRow += direction[move % 4][0]
            startCol += direction[move % 4][1]
        return(ret)