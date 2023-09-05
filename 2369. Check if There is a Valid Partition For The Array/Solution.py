class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        length, mySet = len(nums), set()
        mySet.add(length)

        if(nums[length - 1] == nums[length - 2]):
            mySet.add(length - 2)

        for idx in range(length - 3, -1, -1):
            if(nums[idx] == nums[idx + 1] == nums[idx + 2] and (idx + 3) in mySet):
                mySet.add(idx)
            if(nums[idx] == (nums[idx + 1] - 1) and nums[idx + 1] == (nums[idx + 2] - 1) and (idx + 3) in mySet):
                mySet.add(idx)
            if(nums[idx] == nums[idx + 1] and (idx + 2) in mySet):
                mySet.add(idx)
        
        return(True if 0 in mySet else False)