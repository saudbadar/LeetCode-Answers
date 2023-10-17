class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length, DP = len(cost), [0 for _ in range(len(cost))]
        DP[-2:] = cost[-2:]
        for i in reversed(range(length - 2)):
            DP[i] = cost[i] + min(DP[i + 2], DP[i+1])
        return(min(DP[0], DP[1]))