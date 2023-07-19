class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ret, prevEnd = 0, -sys.maxsize
        
        for start, end in intervals:
            if(prevEnd > start):
                ret += 1
            else:
                prevEnd = end
        return(ret)