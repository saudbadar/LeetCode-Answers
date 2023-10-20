class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph, DP, mySet = [[] for _ in range(n)], [-1 for _ in range(n)], set()

        for i in range(n):
            mySet.add(i)

        for prev, next in relations:
            newVal = next - 1
            graph[newVal].append(prev - 1)
            if(newVal in mySet):
                mySet.remove(newVal)

        for pos in mySet:
            DP[pos] = time[pos]
        
        def findTime(loc):
            if(DP[loc] != -1):
                return(DP[loc])
            maxTime = 0
            for pre in graph[loc]:
                localMax = DP[pre]
                if(DP[pre] == -1):
                    localMax = findTime(pre)
                maxTime = max(localMax, maxTime)
            DP[loc] = maxTime + time[loc]
            return(DP[loc])
        ret = 0
        for i in range(n):
            ret = max(ret, findTime(i))
        return(ret)
                
        