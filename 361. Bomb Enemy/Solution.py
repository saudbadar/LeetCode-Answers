class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rowMax, colMax = len(grid), len(grid[0])
        board = [[0 for _ in range(colMax)] for _ in range(rowMax)]

        def increase(lst, target):
            nonlocal board
            for startRow, startCol in lst:
                board[startRow][startCol] += target
        
        def fillBoard(lengthRow, lengthCol, switch):
            for row in range(lengthRow):
                queue, enemy = [], 0
                for col in range(lengthCol):
                    if(switch):
                        val = grid[col][row]
                    else:
                        val = grid[row][col]
                    if(val == '0'):
                        if(switch):
                            queue.append((col, row))
                        else:
                            queue.append((row, col))
                    elif(val == 'E'):
                        enemy += 1
                    else:
                        increase(queue, enemy)
                        queue, enemy = [], 0
                increase(queue, enemy)
        
        fillBoard(rowMax, colMax, False)
        fillBoard(colMax, rowMax, True)
        return(max((max(x) for x in board)))