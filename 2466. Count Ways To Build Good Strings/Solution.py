class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + 1)]
        dp[0], ret, mod = 1, 0, 10 ** 9 + 7

        for i in range(0, high + 1):
            if((i + zero) <= high):
                dp[i + zero] += dp[i]
            if((i + one) <= high):
                dp[i + one] += dp[i]
            dp[i] %= mod
            if(i >= low):
                ret += dp[i]

        return(ret % mod)