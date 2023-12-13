class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstVal, secondVal = 0, 0
        for num in nums:
            if(num >= firstVal):
                secondVal, firstVal = firstVal, num
            else:
                secondVal = max(secondVal, num)
        return((firstVal - 1) * (secondVal - 1))