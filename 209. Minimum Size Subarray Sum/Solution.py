class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret, left, tempSum = sys.maxsize, 0, 0
        for right, num in enumerate(nums):
            tempSum += num
            while((tempSum >= target) and (right >= left)):
                ret = min(ret, (right - left) + 1)
                tempSum -= nums[left]
                left += 1
        return(ret if ret != sys.maxsize else 0)