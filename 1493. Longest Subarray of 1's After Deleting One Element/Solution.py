class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev, curr, longest = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                curr += 1
            else:
                longest = max(longest, prev + curr)
                prev, curr = curr, 0
        longest = max(longest, prev + curr)
        return longest - 1 if longest == len(nums) else longest