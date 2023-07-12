class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isSafe, visited, ret = set(), set(), []

        def DFS(node):
            nonlocal isSafe, visited
            check = True
            visited.add(node)
            for newNode in graph[node]:
                if(newNode in visited):
                    if(newNode not in isSafe):
                        check = False
                elif(not DFS(newNode)):
                    check = False
            if(check):
                isSafe.add(node)
                return(True)
            return(False)

        for i in range(len(graph)):
            if(i not in visited):
                DFS(i)
            if(i in isSafe):
                ret.append(i)
        return(ret)