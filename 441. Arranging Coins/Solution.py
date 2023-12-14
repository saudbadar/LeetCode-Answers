class Solution:
    def arrangeCoins(self, n: int) -> int:
        return(math.floor(math.sqrt(2) * math.sqrt(0.125 + n) - 0.5))
        