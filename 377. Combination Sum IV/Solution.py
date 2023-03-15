class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]

        for num in nums:
            if(num <= target):
                dp[num] += 1

        for i in range(1, target + 1):
            if(dp[i] == 0):
                continue
            for num in nums:
                pos = i + num
                if(pos <= target):
                    dp[pos] += dp[i]
        return(dp[-1])