class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        ret, lastVal = 1, pairs[0][1]
        for start, end in pairs[1:]:
            if(start > lastVal):
                lastVal = end
                ret += 1
        return(ret)