class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAlt, ret = 0, 0
        for num in gain:
            curAlt += num
            ret = max(ret, curAlt)
        return(ret)