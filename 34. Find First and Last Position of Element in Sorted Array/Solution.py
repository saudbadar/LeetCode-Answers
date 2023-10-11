class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, posLeft, posRight = 0, len(nums) - 1, -1, -1
        while(left <= right):
            middle = (left + right) // 2
            if(nums[middle] == target):
                posLeft = middle
            if(nums[middle] >= target):
                right = middle - 1
            else:
                left = middle + 1
        left, right = 0, len(nums) - 1
        while(left <= right):
            middle = (left + right) // 2
            if(nums[middle] == target):
                posRight = middle
            if(nums[middle] <= target):
                left = middle + 1
            else:
                right = middle - 1
        return([posLeft, posRight])