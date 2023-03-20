class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        curPos, length = 0, len(flowerbed)
        while(curPos < length):
            if(flowerbed[curPos] == 1):
                curPos += 2
                continue
            if((curPos >= 1 and flowerbed[curPos - 1] == 1) or (curPos < (length - 1) and flowerbed[curPos + 1] == 1)):
                curPos += 1
                continue
            n -= 1
            curPos += 2
        return(True if n <= 0 else False)