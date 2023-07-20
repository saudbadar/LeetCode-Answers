class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        mySet, firstMax, secondMax, thirdMax = set(), max(nums), -sys.maxsize, -sys.maxsize
        for num in nums:
            if(num != firstMax):
                secondMax = max(secondMax, num)
        for num in nums:
            if((num != firstMax) and (num != secondMax)):
                thirdMax = max(thirdMax, num)
        return(firstMax if (secondMax == -sys.maxsize or thirdMax == -sys.maxsize) else thirdMax)