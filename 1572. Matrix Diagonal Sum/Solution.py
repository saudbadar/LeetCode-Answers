class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left, right, ret, mid = 0, len(mat) - 1, 0, len(mat) // 2
        for row in mat:
            ret += (row[left] + row[right])
            left += 1
            right -= 1
        if(len(mat) % 2 == 1):
            ret -= mat[mid][mid]
        return(ret)