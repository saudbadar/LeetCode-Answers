class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def areSimilar(stringOne, stringTwo):
            count = 0
            for letterOne, letterTwo in zip(stringOne, stringTwo):
                if(letterOne != letterTwo):
                    count += 1
            return(True if count == 2 or count == 0 else False)

        def DFS(a):
            nonlocal visited
            visited[a] = True
            for j in range(len(strs)):
                if(visited[j]):
                    continue
                if(areSimilar(strs[a], strs[j])):
                    DFS(j)

        ret, length = 0, len(strs)
        visited = [False for _ in range(length)]
        for i in range(length):
            if(visited[i]):
                continue
            ret += 1
            DFS(i)
        return(ret)