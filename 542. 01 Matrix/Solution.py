class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        seen, rowMax, colMax, queue = set(), len(mat), len(mat[0]), deque()
        direction = [[0,1], [1,0], [-1,0], [0,-1]]

        for row in range(rowMax):
            for col in range(colMax):
                if(mat[row][col] == 0):
                    seen.add((row,col))
                    queue.append([row, col, 0])
        while(queue):
            row, col, depth = queue.popleft()
            for move in direction:
                newRow, newCol = row + move[0], col + move[1]
                if(0 <= newRow < rowMax and 0 <= newCol < colMax and (newRow, newCol) not in seen):
                    seen.add((newRow, newCol))
                    mat[newRow][newCol] = depth + 1
                    queue.append([newRow, newCol, depth + 1])
        return(mat)