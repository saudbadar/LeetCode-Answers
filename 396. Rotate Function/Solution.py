class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        newNums, length, sumRight, total = deque(nums), len(nums) - 1, 0, 0
        for idx, num in enumerate(nums[1:]):
            sumRight += (num * (idx + 1))
            total += num
        
        ret = sumRight

        for i in range(length):
            rightMost = newNums.pop()
            sumRight -= (rightMost * length)
            total -= rightMost
            total += newNums[0]
            sumRight += total
            newNums.appendleft(rightMost)
            ret = max(ret, sumRight)
        return(ret)