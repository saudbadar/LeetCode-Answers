class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, maxLen, left, curSum = sum(nums) - x, -1, 0, 0
        for right, num in enumerate(nums):
            curSum += num
            while(left <= right and curSum > target):
                curSum -= nums[left]
                left += 1
            if(curSum == target):
                maxLen = max(maxLen, right - left + 1)
        return(maxLen if maxLen == -1 else len(nums) - maxLen)