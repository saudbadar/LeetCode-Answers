class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        moves, length = 0, len(nums)
        for i in range(1, length):
            diff = ((moves + nums[i]) - nums[i - 1])
            nums[i] += moves
            moves += diff
        return(moves)