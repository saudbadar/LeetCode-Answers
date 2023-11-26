class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            minVal, maxVal = min(arr), max(arr)

            if((maxVal - minVal) % (len(arr) - 1) != 0):
                return(False)
            
            diff = (maxVal - minVal) / (len(arr) - 1)
            arrSet = set(arr)
            curr = minVal + diff
            while(curr < maxVal):
                if(curr not in arrSet):
                    return(False)
                curr += diff
            return(True)