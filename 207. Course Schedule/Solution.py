class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj, valid = [[] for _ in range(numCourses)], [None for _ in range(numCourses)]

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])
        
        def DFS(node):
            nonlocal valid
            valid[node] = False
            for newNode in adj[node]:
                if(valid[newNode] == True):
                    continue
                if(valid[newNode] == False):
                    return(False)
                if(not DFS(newNode)):
                    return(False)
            valid[node] = True
            return(True)

        for i in range(numCourses):
            if(not valid[i]):
                if(not DFS(i)):
                    return(False)
        return(True)