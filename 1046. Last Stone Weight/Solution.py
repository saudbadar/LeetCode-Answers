class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(stones):
            stoneOne = stones.pop()
            if(not stones):
                return(stoneOne)
            stoneTwo = stones.pop()
            if(stoneOne != stoneTwo):
                 bisect.insort(stones, stoneOne - stoneTwo)
        return(0)