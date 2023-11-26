class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        length, loop, ret = len(piles), len(piles) // 3, 0
        for i in range(loop):
            ret += piles[(length - 2) - (2 * i)]
        return(ret)