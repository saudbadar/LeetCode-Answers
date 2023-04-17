class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        length, maxNum = len(candies), max(candies)
        ret = [False for _ in range(length)]
        
        for idx, candy in enumerate(candies):
            if((candy + extraCandies) >= maxNum):
                ret[idx] = True
        return(ret)