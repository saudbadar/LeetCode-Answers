class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ret = prices[0], 0
        for sell in prices[1:]:
            if(sell < buy):
                buy = sell
            else:
                ret = max(ret, sell - buy)
        return(ret)