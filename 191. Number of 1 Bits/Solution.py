class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while(n):
            if(n & 1):
                ret += 1
            n >>= 1
        return(ret)