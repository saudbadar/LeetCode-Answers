class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLength, colLength = len(matrix), len(matrix[0])
        totalSum, counter, ret, startRow, startCol = rowLength * colLength, 1, [], 0, 0
        direction = [[0,1],[1,0], [0,-1], [-1,0]]
        ret.append(matrix[0][0])
        matrix[0][0] = -101
        while True:
            for shiftUp, shiftRight in direction:
                tempRow, tempCol = startRow + shiftUp, startCol + shiftRight
                while(0 <= tempRow < rowLength and 0 <= tempCol < colLength and matrix[tempRow][tempCol] != -101):
                    startRow, startCol = tempRow, tempCol
                    ret.append(matrix[startRow][startCol])
                    matrix[startRow][startCol] = -101
                    tempRow, tempCol = startRow + shiftUp, startCol + shiftRight
                    counter +=1
            if(counter == totalSum):
                return(ret)