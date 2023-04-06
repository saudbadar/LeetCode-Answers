class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ret, totalSum = 0, 0 
        for idx, num in enumerate(nums):
            totalSum += num
            ret = max(ret, math.ceil(totalSum / (idx + 1)))
        return ret