class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ret, streak = 0, 0

        for num in nums:
            if(num == 0):
                ret += (streak + 1)
                streak += 1
            else:
                streak = 0
        return(ret)