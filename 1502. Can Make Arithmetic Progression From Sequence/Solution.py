class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference = arr[1] - arr[0]
        for idx in range(2, len(arr)):
            if((arr[idx] - arr[idx - 1]) != difference):
                return(False)
        return(True)