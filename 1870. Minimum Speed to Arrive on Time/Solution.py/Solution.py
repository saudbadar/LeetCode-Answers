class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def test(speed):
            total = 0
            for num in dist[:-1]:
                total += (num // speed)
                if((num % speed) != 0):
                    total += 1
            total += (dist[-1] / speed)
            if(total <= hour):
                return(True)
            return(False)
        
        left, right, ret = 1, 10**7, None
        while(left <= right):
            middle = left + (right - left) // 2
            if(test(middle)):
                ret = middle
                right = middle - 1
            else:
                left = middle + 1 
        return(ret if ret else -1)