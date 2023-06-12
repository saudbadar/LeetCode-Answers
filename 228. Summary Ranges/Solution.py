class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(not nums):
            return()
        leftVal, rightVal, ret = nums[0], None, []
        for idx, num in enumerate(nums[1:]):
            if(num == (nums[idx] + 1)):
                rightVal = num
            else:
                if(rightVal == None):
                    ret.append(str(leftVal))
                else:
                    ret.append(str(leftVal) + "->" + str(rightVal))
                leftVal, rightVal = num, None
        if(rightVal == None):
            ret.append(str(leftVal))
        else:
            ret.append(str(leftVal) + "->" + str(rightVal))
        return(ret)