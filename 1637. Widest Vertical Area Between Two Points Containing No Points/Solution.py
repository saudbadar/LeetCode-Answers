class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        ret, length = 0, len(points)
        for idx in range(1, length):
            ret = max(ret, points[idx][0] - points[idx - 1][0])
        return(ret)