class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if(len(nums) < 2):
            return(len(nums))
        up, down = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
        up[0], down[0] = 1, 1
        
        for i in range(1, len(nums)):
            if(nums[i] > nums[i - 1]):
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif(nums[i] < nums[i - 1]):
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return(max(up[-1], down[-1]))
