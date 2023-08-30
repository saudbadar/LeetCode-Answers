class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        rightMost, ret = nums.pop(), 0
        while(nums):
            num = nums.pop()
            div = (num + rightMost - 1) // rightMost
            ret += (div - 1)
            rightMost = num // div
        return(ret)