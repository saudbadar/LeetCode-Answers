class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst, rowMax, colMax, ret = [], len(mat), len(mat[0]), []
        for row in range(rowMax):
            numOfOnes = 0
            for col in range(colMax):
                if(mat[row][col] == 0):
                    break
                numOfOnes += 1
            lst.append([numOfOnes, row])
        lst.sort()
        ret = [tempLst[1] for tempLst in lst[:k]]
        return(ret)