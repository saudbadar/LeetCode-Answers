class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev, increase = nums[0], 0
        for num in nums[1:]:
            if(prev < num):
                if(increase == -1):
                    return(False)
                increase = 1
            if(prev > num):
                if(increase == 1):
                    return(False)
                increase = -1
            prev = num
        return(True)