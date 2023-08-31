class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        tapReach, tapUsed = [0 for _ in range(n + 1)], 0
        
        for idx, dis in enumerate(ranges):
            if(dis == 0):
                continue
            leftReach, rightReach = max(0, idx - dis), min(n, idx + dis)
            tapReach[idx] = rightReach
            tapReach[leftReach] = max(tapReach[leftReach], rightReach)
        
        end, curReach = 0, 0
        for loc, reach in enumerate(tapReach):
            if(loc > end):
                if(curReach <= end):
                    return(-1)
                end = curReach
                tapUsed += 1
            curReach = max(curReach, reach)
        return(tapUsed)