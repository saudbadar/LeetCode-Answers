class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if(len(nums) < 3):
            return(0)
        count, length = 0, len(nums)

        for idx in range(1, length - 1):
            diff = nums[idx] - nums[idx + 1]
            for newIdx in range(idx - 1, -1, -1):
                if((nums[newIdx] - nums[newIdx + 1]) == diff):
                    count += 1
                else:
                    break
        return(count)