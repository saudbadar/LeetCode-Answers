class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(maxSum, maxCuts):
            numOfCuts, curSum = 0, 0
            for num in nums:
                curSum += num
                if(curSum > maxSum):
                    curSum = num
                    numOfCuts += 1
                    if(numOfCuts >= maxCuts):
                        return(False)
            return(True)

        low, high = max(nums), sum(nums)
        while(low < high):
            middle = low + (high - low) // 2
            if(canSplit(middle, k)):
                high = middle
            else:
                low = middle + 1
        return(low)