class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employee, queue, ret = defaultdict(list), deque([headID]), 0

        for idx, boss in enumerate(manager):
            if(idx == headID):
                continue
            employee[boss].append(idx)
        
        def DFS(pos, timeTaken):
            nonlocal ret
            if(informTime[pos] == 0):
                ret = max(ret, timeTaken)
                return
            for people in employee[pos]:
                DFS(people, timeTaken + informTime[pos])

        DFS(headID, 0)
        return(ret)