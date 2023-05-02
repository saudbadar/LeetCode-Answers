class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num = 1
        for i in nums:
            num *= i
        if num > 0:
            return 1
        elif num == 0:
            return 0
        else:
            return -1