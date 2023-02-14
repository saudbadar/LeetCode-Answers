class Solution:
    def integerBreak(self, n: int) -> int:
        DP = {1: 1, 2: 2, 3: 3, 4: 4, 5: 6, 6: 9}
        ret = {1: 1, 2: 1, 3: 2, 4: 4}
        if(n <= 4):
            return(ret[n])

        for i in range(5, n + 1):
            DP[i] = 0
            for j in range(2, (i // 2) + 1):
                DP[i] = max(DP[i], DP[i-j] * DP[j])
        return(DP[n])