class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret, length, add = 0, len(points), {1: 0, 2: 2, 3: 6, 4: 12}

        for i in range(length):
            myDict = {}
            for j in range(length):
                if(i == j):
                    continue
                dist = math.dist(points[i], points[j])
                if(dist in myDict):
                    ret += ((myDict[dist]) * 2)
                myDict[dist] = myDict.get(dist, 0) + 1
        return(ret)
        