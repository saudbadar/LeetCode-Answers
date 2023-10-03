class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        myDict, ret = {}, 0
        for num in nums:
            myDict[num] = myDict.get(num, 0)
            ret += myDict[num]
            myDict[num] += 1
        return(ret)