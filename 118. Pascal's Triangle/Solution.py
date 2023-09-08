class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret, lst = [[1]], [1]
        for i in range(1, numRows):
            temp = lst.copy()
            for j in range(1, len(lst)):
                lst[j] = temp[j] + temp[j - 1]
            lst.append(1)
            ret.append(lst.copy())
        return(ret)