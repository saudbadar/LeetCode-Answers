class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [0 for i in range(len(isConnected))]

        def find(lst, i):
            if(i != lst[i]):
                lst[i] = find(lst, lst[i])
            return(lst[i])
        
        def union(lst, x, y):
            xRoot = find(lst, x)
            yRoot = find(lst, y)
            if(xRoot == yRoot):
                return
            elif(rank[x] > rank[y]):
                parent[yRoot] = xRoot
            elif(rank[y] > rank[x]):
                parent[xRoot] = yRoot
            else:
                parent[xRoot] = yRoot
                rank[yRoot] += 1
        
        for x in range(len(isConnected)):
            for y in range(len(isConnected)):
                if(x == y):
                    continue
                if(isConnected[x][y] == 1):
                    union(parent, x, y)
        return(len(set([find(parent, i) for i in range(len(isConnected))])))