class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rowMax, colMax, mySet = len(board), len(board[0]), set()

        for row in range(rowMax):
            for col in range(colMax):
                if(board[row][col] == "X"):
                    if((row - 1, col) in mySet):
                        mySet.remove((row - 1, col))
                    elif((row, col - 1) in mySet):
                        mySet.remove((row, col - 1))
                    mySet.add((row, col))
        return(len(mySet))