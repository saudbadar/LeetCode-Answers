class Solution:
    def numDecodings(self, s: str) -> int:
        dp, idx = [0 for _ in range(len(s) + 1)], len(s) - 2
        dp[-1] = 1
        if(s[-1] != '0'):
            dp[-2] = 1
        if(s[0] == '0'):
            return(0)

        while(idx >= 0):
            ten, one, moves = int(s[idx]), int(s[idx + 1]), 0
            if(ten == 0):
                dp[idx] = 0
                idx -= 1
                continue
            ten = ten * 10 + one
            moves += dp[idx + 1]
            if(10 <= ten <= 26):
                moves += dp[idx + 2]
            dp[idx] = moves
            idx -= 1
        return(dp[0])