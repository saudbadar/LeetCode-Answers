class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        colored = [-1 for _ in range(length)]

        def DFS(node, color):
            nonlocal colored
            colored[node] = color

            for neigbour in graph[node]:
                if(colored[neigbour] == -1):
                    if(not DFS(neigbour, 1 - color)):
                        return(False)
                elif(colored[neigbour] == color):
                    return(False)
            return(True)
        
        for i in range(length):
            if(colored[i] == -1):
                if(not DFS(i, 0)):
                    return(False)
        return(True)