class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited, adjacent, ret = set(), [[] for _ in range(n)], 0

        for connection in connections:
            adjacent[connection[0]].append((connection[1], 0))
            adjacent[connection[1]].append((connection[0], 1))
        
        def DFS(node):
            nonlocal visited, ret
            visited.add(node)
            for newCity, toFrom in adjacent[node]:
                if(newCity not in visited):
                    if(not toFrom):
                        ret += 1
                    DFS(newCity)
        DFS(0)
        return(ret)