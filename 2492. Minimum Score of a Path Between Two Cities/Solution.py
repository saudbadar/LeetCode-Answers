class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        connected, ret, visited = [[] for _ in range(n + 1)], sys.maxsize, set()

        for road in roads:
            connected[road[0]].append([road[1], road[2]])
            connected[road[1]].append([road[0], road[2]])

        def DFS(currentLoc):
            nonlocal ret, visited
            for city in connected[currentLoc]:
                ret = min(city[1], ret)
                if(city[0] not in visited):
                    visited.add(city[0])
                    DFS(city[0])
        DFS(1)
        return(ret)