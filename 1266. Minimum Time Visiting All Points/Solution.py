class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ret, [startX, startY] = 0, points[0]
        for newX, newY in points[1:]:
            ret += max(abs(newX - startX), abs(newY - startY))
            startX, startY = newX, newY
        return(ret)