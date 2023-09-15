class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
        myDict, length = defaultdict(list), len(points)
        for i in range(length):
            for j in range(i + 1, length):
                val = distance(points[i], points[j])
                myDict[i].append((val, j))
                myDict[j].append((val, i))
        ret, heap, seen, count = 0, myDict[0], [0] * length, 0
        seen[0] = 1
        heapq.heapify(heap)
        while(heap):
            dist, newPoint = heapq.heappop(heap)
            if(not seen[newPoint]):
                seen[newPoint], count, ret = 1, count + 1, ret + dist
                for record in myDict[newPoint]:
                    heapq.heappush(heap, record)
            if(count >= length):
                break
        return(ret)