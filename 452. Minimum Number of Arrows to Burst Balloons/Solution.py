class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ret, endLoc = 0, points[0][1]
        for point in points[1:]:
            if(endLoc < point[0]):
                ret += 1
                endLoc = point[1]
        return(ret + 1)