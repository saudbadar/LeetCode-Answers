class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret, length = [], len(nums)
        for i in range(length):
            newIndex = abs(nums[i]) - 1
            if(nums[newIndex] > 0):
                nums[newIndex] *= -1
        
        for i in range(1, length + 1):
            if(nums[i - 1] > 0):
                ret.append(i)
        return(ret)