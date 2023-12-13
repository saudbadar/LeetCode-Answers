class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        colSum, ret = set(), 0
        def getColSum(colIdx):
            nonlocal colSum
            sumOf = 0
            for row in mat:
                sumOf += row[colIdx]
            colSum.add(colIdx)
            return(sumOf)
        for row in mat:
            if(sum(row) == 1):
                colIdx = row.index(1)
                if(colIdx not in colSum):
                    ret += (getColSum(colIdx) == 1)
        return(ret)