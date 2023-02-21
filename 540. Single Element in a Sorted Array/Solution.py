class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L, R, mid, ans = 0, len(nums)-1, 0, 0
        while L <= R:
            mid = ((L + R) >> 2) << 1 
            if mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                L = mid + 2
            else: 
                R, ans = mid - 1, nums[mid]
        return ans