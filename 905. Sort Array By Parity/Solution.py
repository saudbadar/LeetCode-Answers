class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddPos = 0
        for idx, num in enumerate(nums):
            if((num % 2) == 0):
                nums[idx], nums[oddPos] = nums[oddPos], nums[idx]
                oddPos += 1
        return(nums)