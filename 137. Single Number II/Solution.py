class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for i in range(32):
            mask, count = 1 << i, 0
            for num in nums:
                if(mask & num):
                    count += 1
            if((count % 3) != 0):
                ret |= mask
            if(ret & 1 << 31):
                ret -= 2 ** 32 
        return(ret)