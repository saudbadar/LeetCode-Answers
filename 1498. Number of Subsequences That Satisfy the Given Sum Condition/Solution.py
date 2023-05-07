class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ret, module, left, right = 0, (10 ** 9) + 7, 0, len(nums) - 1
        nums.sort()
        
        while left <= right:
            if((nums[left] + nums[right]) > target):
                right -= 1
            else:
                ret = (ret + pow(2, right - left)) % module
                left += 1
        return(ret)