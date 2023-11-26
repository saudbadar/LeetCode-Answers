class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ret, prefixSum, totalSum, length = [], 0, sum(nums), len(nums) - 1
    
        for idx, num in enumerate(nums):
            totalSum -= num
            leftSide, rightSide = 0, 0
            rightSide = totalSum - (length - idx) * num
            leftSide = (num * idx) - prefixSum
            ret.append(leftSide + rightSide)
            prefixSum += num
        return(ret)
        