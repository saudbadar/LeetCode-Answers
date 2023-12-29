class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ret, gPos, sPos, gLen, sLen = 0, 0, 0, len(g), len(s)
        while(gPos < gLen and sPos < sLen):
            if(g[gPos] <= s[sPos]):
                gPos += 1
                ret += 1
            sPos += 1
        return(ret)