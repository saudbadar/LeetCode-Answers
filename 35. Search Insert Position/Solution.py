class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            ret(-1)
        
        start, end = 0, len(nums) - 1
        
        while(start <= end):
            mid = start + int((end - start)/2)
            
            if(nums[mid] < target):
                start = mid + 1
            elif(nums[mid] > target):
                end = mid - 1
            else:
                return(mid)
        
        return(max(start,end))