class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix, rowMax, colMax = [[] for _ in range(len(matrix[0]))], len(matrix), len(matrix[0])

        for row in range(rowMax):
            for col in range(colMax):
                newMatrix[col].append(matrix[row][col])
        return(newMatrix)
        