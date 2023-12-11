class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ret, lst = [], []
        for idx, interval in enumerate(intervals):
            lst.append([interval[0], idx])
        lst.append([float('inf'), -1])
        lst.sort()
        for arr in intervals:
            val = lst[bisect_left(lst, [arr[1]])][1]
            ret.append(val)
        return(ret)