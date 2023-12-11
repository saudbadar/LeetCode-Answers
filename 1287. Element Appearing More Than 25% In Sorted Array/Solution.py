class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        lst, limit = [-1, 0], len(arr) // 4 + 1
        for val in arr:
            if(val != lst[0]):
                lst = [val, 1]
            else:
                lst[1] += 1
            if(lst[1] >= limit):
                return(val)
        return(-1)