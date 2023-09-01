class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while(left <= right):
            middle = (left + right) // 2
            val = nums[middle]
            if(val == target):
                return(middle)
            if(val >= nums[left]):
                if(val > target and target >= nums[left]):
                    right = middle - 1
                else:
                    left = middle + 1
            elif(val < nums[right]):
                if(val < target and target <= nums[right]):
                    left = middle + 1
                else:
                    right = middle - 1  
        return(-1)