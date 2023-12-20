class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ret = money - prices[1] - prices[0]
        if(ret < 0):
            return(money)
        return(ret)